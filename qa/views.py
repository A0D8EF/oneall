from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q

from .models import Tag, Question, Answer
from .forms import QuestionTagForm, QuestionForm, AnswerForm

class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context         = {}
        context["tags"] = Tag.objects.all()

        query   = Q()
        if "search" in request.GET:
            search      = request.GET["search"]
            raw_words   = search.replace("　"," ").split(" ")
            words       = [ w for w in raw_words if w != "" ]

            for w in words:
                query   &= Q(title__contains=w)
        
        questions       = Question.objects.filter(query).order_by("-dt")

        form    = QuestionTagForm(request.GET)
        if form.is_valid():
            cleaned         = form.clean()
            selected_tags   = cleaned["tag"] #Tagモデルオブジェクトのリスト型

            for tag in selected_tags:
                questions   = [ question for question in questions if tag in question.tag.all() ]
        
        context["questions"]    = questions

        return render(request, "qa/index.html", context)

    def post(self, request, *args, **kwargs):
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form            = QuestionForm(copied)
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("qa:index")
        
        form.save()

        return redirect("qa:index")
    
index = IndexView.as_view()


class QuestionGoodView(LoginRequiredMixin,View):
    def post(self, request, pk, *args, **kwargs):

        question    = Question.objects.filter(id=pk).first()

        if request.user in question.good.all():
            question.good.remove(request.user)
        else:
            question.good.add(request.user)

        return redirect("qa:detail", pk)

question_good = QuestionGoodView.as_view()


class DetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context             = {}
        context["tags"] = Tag.objects.all()
        context["question"] = Question.objects.filter(id=pk).first()
        context["answers"]  = Answer.objects.filter(target=pk).order_by("dt")

        return render(request, "qa/detail.html", context)

    def post(self, request, pk, *args, **kwargs):
        copied              = request.POST.copy()
        copied["user"]      = request.user.id
        copied["target"]    = Question.objects.filter(id=pk).first()

        form            = AnswerForm(copied)
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("qa:detail", pk)
        
        form.save()

        return redirect("qa:detail", pk)

detail = DetailView.as_view()


class AnswerGoodView(LoginRequiredMixin,View):
    def post(self, request, q_id, a_id, *args, **kwargs):

        answer      = Answer.objects.filter(id=a_id).first()

        if request.user in answer.good.all():
            answer.good.remove(request.user)
        else:
            answer.good.add(request.user)
        
        return redirect("qa:detail", q_id)


answer_good = AnswerGoodView.as_view()

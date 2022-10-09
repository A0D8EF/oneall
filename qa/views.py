from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q

from .models import Tag, Question
from .forms import QuestionTagForm, QuestionForm

class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context = {}
        context["tags"]         = Tag.objects.all()

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
            print(selected_tags)

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


class GoodView(LoginRequiredMixin,View):
    def post(self, request, pk, *args, **kwargs):

        question    = Question.objects.filter(id=pk).first()

        if request.user in question.good.all():
            question.good.remove(request.user)
        else:
            question.good.add(request.user)

        return redirect("qa:index")


good = GoodView.as_view()
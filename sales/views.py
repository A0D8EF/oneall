from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q

from .models import AC, Question, ABC, Interview, Contract
from .forms import ACForm, QuestionForm, ABCForm, InterviewForm, ContractForm, YearMonthForm

from . import calender

import datetime

from django.http import HttpResponseNotFound
from django.template.loader import render_to_string


class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context = {}

        form    = YearMonthForm(request.GET)
        today   = datetime.datetime.now()

        if form.is_valid():
            cleaned = form.clean()

            selected_date   = datetime.datetime(year=cleaned["year"], month=cleaned["month"], day=1).astimezone()
        else:
            selected_date   = datetime.datetime(year=today.year, month=today.month, day=1).astimezone()

        context["selected_date"] = selected_date

        context["months"]    = [ i for i in range(1,13) ]

        context["years"]    = calender.create_years(request, selected_date, today)
        context["next_month"], context["last_month"]    = calender.create_months(selected_date)
        context["calender"]       = calender.create_calender(selected_date.year, selected_date.month)

        if request.user.is_teacher:
            context["acs"]          = AC.objects.all().order_by("-ac_date")
            context["questions"]    = Question.objects.all().order_by("-q_date")
            context["abcs"]         = ABC.objects.all().order_by("-abc_date")
            context["interviews"]   = Interview.objects.all().order_by("-interview_date")
            context["contracts"]    = Contract.objects.all().order_by("-contract_date")
        else:
            context["acs"]          = AC.objects.filter(user=request.user.id).order_by("-ac_date")
            context["questions"]    = Question.objects.filter(user=request.user.id).order_by("-q_date")
            context["abcs"]         = ABC.objects.filter(user=request.user.id).order_by("-abc_date")
            context["interviews"]   = Interview.objects.filter(user=request.user.id).order_by("-interview_date")
            context["contracts"]    = Contract.objects.filter(user=request.user.id).order_by("-contract_date")

        return render(request, "sales/index.html", context)
    
    def post(self, request, *args, **kwargs):
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        if copied["sales_form_chk"] == "ac":
            form        = ACForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
        elif copied["sales_form_chk"] == "question":
            form        = QuestionForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
        elif copied["sales_form_chk"] == "abc":
            form        = ABCForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
        elif copied["sales_form_chk"] == "interview":
            form        = InterviewForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
        else:
            form        = ContractForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
        
        form.save()

        return redirect("sales:index")


index = IndexView.as_view()


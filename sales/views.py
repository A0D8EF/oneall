from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q
from django.db.models import Sum

from .models import AC, Question, ABC, Interview, Contract
from .forms import ACForm, QuestionForm, ABCForm, InterviewForm, ContractForm, YearMonthForm

from . import calender

import datetime

from django.http import HttpResponseNotFound
from django.template.loader import render_to_string

from  pytz import timezone


class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context = {}

        form    = YearMonthForm(request.GET)

        jst     = timezone('Asia/Tokyo')
        today   = datetime.datetime.now(tz=jst)
        if form.is_valid():
            cleaned = form.clean()
            selected_date   = datetime.datetime(year=cleaned["year"], month=cleaned["month"], day=1, tzinfo=jst)
        else:
            selected_date   = datetime.datetime(year=today.year, month=today.month, day=1, tzinfo=jst)

        context["selected_date"] = selected_date

        context["months"]   = [ i for i in range(1,13) ]
        context["years"]    = calender.create_years(request, selected_date, today)
        context["next_month"], context["last_month"]    = calender.create_months(selected_date)
        context["calender"] = calender.create_calender(selected_date.year, selected_date.month)

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
        
        # 月間データ
        monthly_sales_data  = []
        dic                 = {}
        query               = Q( user=request.user.id, ac_date__year=selected_date.year, ac_date__month=selected_date.month )
        monthly_ac          = AC.objects.filter(query).count()

        query               = Q( user=request.user.id, q_date__year=selected_date.year, q_date__month=selected_date.month )
        monthly_question    = Question.objects.filter(query).count()
        
        query               = Q( user=request.user.id, abc_date__year=selected_date.year, abc_date__month=selected_date.month )
        monthly_abc         = ABC.objects.filter(query).count()
        
        query               = Q( user=request.user.id, interview_date__year=selected_date.year, interview_date__month=selected_date.month )
        monthly_interview   = Interview.objects.filter(query).count()
        
        query               = Q( user=request.user.id, contract_date__year=selected_date.year, contract_date__month=selected_date.month )
        monthly_contract    = Contract.objects.filter(query).count()
        
        dic["acs"]          = monthly_ac
        dic["questions"]    = monthly_question
        dic["abcs"]         = monthly_abc
        dic["interviews"]   = monthly_interview
        dic["contracts"]    = monthly_contract
        monthly_sales_data.append(dic)

        context["monthly_sales_datas"]  = monthly_sales_data
        
        # 年間データ
        yearly_sales_data       = []
        for i in range(0,12):
            dic                 = {}
            year                = int(selected_date.year)
            month               = int(selected_date.month)-i
            if month < 1:
                year    = int(selected_date.year)-1
                month   = 12 + month
            yearly_ac           = AC.objects.filter(user=request.user.id, ac_date__year=year, ac_date__month=month).count()
            yearly_question     = Question.objects.filter(user=request.user.id, q_date__year=year, q_date__month=month).count()
            yearly_abc          = ABC.objects.filter(user=request.user.id, abc_date__year=year, abc_date__month=month).count()
            yearly_interview    = Interview.objects.filter(user=request.user.id, interview_date__year=year, interview_date__month=month).count()
            yearly_contract     = Contract.objects.filter(user=request.user.id, contract_date__year=year, contract_date__month=month).count()
            
            dic["year"]         = year
            dic["month"]        = month
            dic["acs"]          = yearly_ac
            dic["questions"]    = yearly_question
            dic["abcs"]         = yearly_abc
            dic["interviews"]   = yearly_interview
            dic["contracts"]    = yearly_contract

            yearly_sales_data.append(dic)
        yearly_sales_data.reverse()

        context["yearly_sales_datas"]   = yearly_sales_data

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


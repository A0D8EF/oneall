from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
from rest_framework.views import APIView as View

from django.db.models import Q
from django.db.models import Sum

from .models import AC, Question, ABC, Interview, Contract
from .forms import ACForm, QuestionForm, ABCForm, InterviewForm, ContractForm, YearMonthForm

from users.models import CustomUser

from . import calender, set_selected_date
from . import term_sales_data, teacher_sales_data
from . import change_status

import datetime

from django.http import HttpResponseNotFound
from django.http.response import JsonResponse
from django.template.loader import render_to_string

from  pytz import timezone


class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context = {}

        jst     = timezone('Asia/Tokyo')
        today   = datetime.datetime.now(tz=jst)

        selected_date               = set_selected_date.set(request, jst, today)
        context["selected_date"]    = selected_date

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

            context["students"]     = CustomUser.objects.filter(is_student=True).order_by("date_joined")
            context["monthly_sales_datas"]  = teacher_sales_data.monthly(request, selected_date)
            context["yearly_sales_datas"]   = teacher_sales_data.yearly(request, selected_date)

        else:
            context["acs"]          = AC.objects.filter(user=request.user.id).order_by("-ac_date")
            context["questions"]    = Question.objects.filter(user=request.user.id).order_by("-q_date")
            context["abcs"]         = ABC.objects.filter(user=request.user.id).order_by("-abc_date")
            context["interviews"]   = Interview.objects.filter(user=request.user.id).order_by("-interview_date")
            context["contracts"]    = Contract.objects.filter(user=request.user.id).order_by("-contract_date")
            
            context["monthly_sales_datas"]  = term_sales_data.monthly(request, selected_date)
            context["yearly_sales_datas"]   = term_sales_data.yearly(request, selected_date)

            change_status.change_inactive(request, today)
            # acs     = AC.objects.filter(user=request.user.id)
            # for ac in acs:
            #     if ac.c_is_ac_active and (ac.ac_date + tz.timedelta(days=21) < today):
            #         print(ac.ac_date)
            #         ac.c_is_ac_active = False
            #         ac.save()
        

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
            
            ac          = AC.objects.filter(id=request.POST["ac"]).first()
            ac.c_is_ac_active  = False
            ac.save()
        elif copied["sales_form_chk"] == "abc":
            form        = ABCForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
            
            q                       = Question.objects.filter(id=request.POST["question"]).first()
            q.c_is_question_active  = False
            q.save()
        elif copied["sales_form_chk"] == "interview":
            form        = InterviewForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
            
            abc                 = ABC.objects.filter(id=request.POST["abc"]).first()
            abc.c_is_abc_active = False
            abc.save()
        else:
            form        = ContractForm(copied)
            if not form.is_valid():
                print("バリデーションNG")
                print(form.errors)
                return redirect("sales:index")
            
            interview                       = Interview.objects.filter(id=request.POST["interview"]).first()
            interview.c_is_interview_active = False
            interview.save()
        
        form.save()

        return redirect("sales:index")


index = IndexView.as_view()


class ACDetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["ac"]   = AC.objects.filter(id=pk).first()
        return render(request, "sales/ac_detail.html", context)
    
    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }
        ac      = AC.objects.filter(id=pk).first()
        if ac:
            ac.delete()
            data["error"] = False

        return JsonResponse(data)
    
    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        ac              = AC.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = ACForm(copied, instance=ac)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)
    
ac_detail = ACDetailView.as_view()


class QuestionDetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["q"]    = Question.objects.filter(id=pk).first()
        context["acs"]  = AC.objects.filter(user=request.user.id).order_by("-ac_date")
        return render(request, "sales/q_detail.html", context)
    
    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }
        q       = Question.objects.filter(id=pk).first()
        if q:
            q.delete()
            data["error"] = False

        return JsonResponse(data)
    
    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        q               = Question.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = QuestionForm(copied, instance=q)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)

q_detail = QuestionDetailView.as_view()


class ABCDetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["abc"]  = ABC.objects.filter(id=pk).first()
        context["questions"]    = Question.objects.filter(user=request.user.id).order_by("-q_date")
        return render(request, "sales/abc_detail.html", context)
        
    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }
        abc     = ABC.objects.filter(id=pk).first()
        if abc:
            abc.delete()
            data["error"] = False

        return JsonResponse(data)
    
    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        abc             = ABC.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = ABCForm(copied, instance=abc)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)

abc_detail = ABCDetailView.as_view()


class InterviewDetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["interview"]    = Interview.objects.filter(id=pk).first()
        context["abcs"]         = ABC.objects.filter(user=request.user.id).order_by("-abc_date")
        return render(request, "sales/interview_detail.html", context)

    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }
        interview   = Interview.objects.filter(id=pk).first()
        if interview:
            interview.delete()
            data["error"] = False

        return JsonResponse(data)
    
    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        interview       = Interview.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = InterviewForm(copied, instance=interview)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)

interview_detail = InterviewDetailView.as_view()


class ContractDetailView(LoginRequiredMixin,View):

    def get(self, request, pk, *args, **kwargs):
        context = {}
        context["contract"]     = Contract.objects.filter(id=pk).first()
        context["interviews"]   = Interview.objects.filter(user=request.user.id).order_by("-interview_date")
        return render(request, "sales/contract_detail.html", context)
        
    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }
        contract    = Contract.objects.filter(id=pk).first()
        if contract:
            contract.delete()
            data["error"] = False

        return JsonResponse(data)
    
    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        contract        = Contract.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = ContractForm(copied, instance=contract)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)

contract_detail = ContractDetailView.as_view()

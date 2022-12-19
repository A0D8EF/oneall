from .models import AC, Question, ABC, Interview, Contract
from users.models import CustomUser

from django.db.models import Q

def monthly(request, selected_date):
    monthly_sales_data  = []

    students            = CustomUser.objects.filter(is_student=True).order_by("date_joined")
    for student in students:
        dic                 = {}
        dic_in_dic          = {}
        query               = Q( user=student.id, ac_date__year=selected_date.year, ac_date__month=selected_date.month )
        monthly_ac          = AC.objects.filter(query).count()

        query               = Q( user=student.id, q_date__year=selected_date.year, q_date__month=selected_date.month )
        monthly_question    = Question.objects.filter(query).count()
    
        query               = Q( user=student.id, abc_date__year=selected_date.year, abc_date__month=selected_date.month )
        monthly_abc         = ABC.objects.filter(query).count()
        
        query               = Q( user=student.id, interview_date__year=selected_date.year, interview_date__month=selected_date.month )
        monthly_interview   = Interview.objects.filter(query).count()
        
        query               = Q( user=student.id, contract_date__year=selected_date.year, contract_date__month=selected_date.month )
        monthly_contract    = Contract.objects.filter(query).count()
    
        dic_in_dic["acs"]          = monthly_ac
        dic_in_dic["questions"]    = monthly_question
        dic_in_dic["abcs"]         = monthly_abc
        dic_in_dic["interviews"]   = monthly_interview
        dic_in_dic["contracts"]    = monthly_contract

        dic = {
            "user": student.username,
            "data": dic_in_dic
        }
        # dic = { {"user": "student1", "data": {"acs": 1, "questions": 2, ... } }

        monthly_sales_data.append(dic)
        # monthly_sales_data = {
        #   {"user": "student1", "data": {"acs": 1, "questions": 2, ... }},
        #   {"user": "student2", "data": {"acs": 1, "questions": 2, ... }},
        #   ...
        # }
    
    dic         = {}
    dic_in_dic  = {}
    dic_in_dic["acs"]          = AC.objects.filter(ac_date__year=selected_date.year, ac_date__month=selected_date.month).count()
    dic_in_dic["questions"]    = Question.objects.filter(q_date__year=selected_date.year, q_date__month=selected_date.month).count()
    dic_in_dic["abcs"]         = ABC.objects.filter(abc_date__year=selected_date.year, abc_date__month=selected_date.month).count()
    dic_in_dic["interviews"]   = Interview.objects.filter(interview_date__year=selected_date.year, interview_date__month=selected_date.month).count()
    dic_in_dic["contracts"]    = Contract.objects.filter(contract_date__year=selected_date.year, contract_date__month=selected_date.month).count()

    dic         = {
        "user": "all",
        "data": dic_in_dic
    }
    monthly_sales_data.append(dic)
    
    return monthly_sales_data


def yearly(request, selected_date):
    yearly_sales_data   = []
    students            = CustomUser.objects.filter(is_student=True).order_by("-date_joined")

    for student in students:
        for i in range(0,12):
            dic                 = {}
            dic_in_dic          = {}
            year                = int(selected_date.year)
            month               = int(selected_date.month)-i
            if month < 1:
                year    = int(selected_date.year)-1
                month   = 12 + month
            yearly_ac           = AC.objects.filter(user=student.id, ac_date__year=year, ac_date__month=month).count()
            yearly_question     = Question.objects.filter(user=student.id, q_date__year=year, q_date__month=month).count()
            yearly_abc          = ABC.objects.filter(user=student.id, abc_date__year=year, abc_date__month=month).count()
            yearly_interview    = Interview.objects.filter(user=student.id, interview_date__year=year, interview_date__month=month).count()
            yearly_contract     = Contract.objects.filter(user=student.id, contract_date__year=year, contract_date__month=month).count()
            
            dic_in_dic["year"]         = year
            dic_in_dic["month"]        = month
            dic_in_dic["acs"]          = yearly_ac
            dic_in_dic["questions"]    = yearly_question
            dic_in_dic["abcs"]         = yearly_abc
            dic_in_dic["interviews"]   = yearly_interview
            dic_in_dic["contracts"]    = yearly_contract
        
            dic = {
                "user": student.username,
                "data": dic_in_dic
            }

            yearly_sales_data.append(dic)

    yearly_sales_data.reverse()
    
    return yearly_sales_data
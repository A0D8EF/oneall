from .models import AC, Question, ABC, Interview, Contract
from django.db.models import Q

def monthly(request, selected_date):
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

    return monthly_sales_data


def yearly(request, selected_date):
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
    
    return yearly_sales_data
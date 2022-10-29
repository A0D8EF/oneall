from django import forms
from .models import AC, Question, ABC, Interview, Contract

from django.core.validators import MinValueValidator, MaxValueValidator


class ACForm(forms.ModelForm):

    class Meta:
        model   = AC
        fields  = ["user","ac_date","c_name","place"]


class QuestionForm(forms.ModelForm):

    class Meta:
        model   = Question
        fields  = ["user","q_date","ac"]
    

class ABCForm(forms.ModelForm):

    class Meta:
        model   = ABC
        fields  = ["user","abc_date","question"]


class InterviewForm(forms.ModelForm):

    class Meta:
        model   = Interview
        fields  = ["user","interview_date","abc"]


class ContractForm(forms.ModelForm):

    class Meta:
        model   = Contract
        fields  = ["user","contract_date","interview"]


# 年月検索用バリデーションフォーム
class YearMonthForm(forms.Form):
    year    = forms.IntegerField()
    month   = forms.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])


from django import forms
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model   = Question
        fields  = ["title","content","user","tag"]


class QuestionTagForm(forms.ModelForm):

    class Meta:
        model   = Question
        fields  = [ "tag" ]
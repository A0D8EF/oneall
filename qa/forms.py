from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):

    class Meta:
        model   = Question
        fields  = ["title","content","user","tag"]


class QuestionTagForm(forms.ModelForm):

    class Meta:
        model   = Question
        fields  = [ "tag" ]


class AnswerForm(forms.ModelForm):

    class Meta:
        model   = Answer
        fields  = ["target", "content", "user"]

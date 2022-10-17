from django import forms
from .models import News

class NewsForm(forms.ModelForm):

    class Meta:
        model   = News
        fields  = ["title","content","user","category"]


class CategorySearchForm(forms.ModelForm):

    class Meta:
        model   = News
        fields  = ["category"]
    
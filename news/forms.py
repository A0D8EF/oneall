from django import forms
from .models import News, Category

class NewsForm(forms.ModelForm):

    class Meta:
        model   = News
        fields  = ["title","content","user","category"]


class CategorySearchForm(forms.ModelForm):

    class Meta:
        model   = News
        fields  = ["category"]


class CategoryForm(forms.ModelForm):

    class Meta:
        model   = Category
        fields  = ["name"]

        error_messages = {
            'name': {
                'max_length': "カテゴリ名が" + str(Category.name.field.max_length) + "文字を超えています。",
                'required': "カテゴリ名を入力してください。",
                'unique' : "同一のカテゴリ名が既に存在します。",
            },
        }
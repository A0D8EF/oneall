from django import forms
from .models import Textbook, MajorCategory, MinorCategory

from django.core.exceptions import ValidationError

class TextbookForm(forms.ModelForm):

    class Meta:
        model   = Textbook
        fields  = ["user", "title", "thumbnail", "thumbnail_url", "file_content", "major_category", "minor_category", "is_youtube", "youtube_url", "is_top", "top_order", "explanation"]
    
    def clean(self):
        data    = self.cleaned_data
        
        if data["is_youtube"]:
            if not data["youtube_url"]:
                raise ValidationError("YoutubeのURLを入力してください")
        else:
            if not data["file_content"]:
                raise ValidationError("ファイルをアップロードしてください")


class MajorCategoryForm(forms.ModelForm):

    class Meta:
        model   = MajorCategory
        fields  = ["name", "order"]

class MinorCategoryForm(forms.ModelForm):

    class Meta:
        model   = MinorCategory
        fields  = ["parent","name", "order"]


class MajorCategorySearchForm(forms.ModelForm):

    class Meta:
        model   = Textbook
        fields  = ["major_category"]


class MinorCategorySearchForm(forms.ModelForm):

    class Meta:
        model   = Textbook
        fields  = ["minor_category"]    


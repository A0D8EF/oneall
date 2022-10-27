from django import forms
from .models import Textbook, MajorCategory

from django.core.exceptions import ValidationError

class TextbookForm(forms.ModelForm):

    class Meta:
        model   = Textbook
        fields  = ["user", "title", "thumbnail", "file_content", "minor_category", "is_youtube", "youtube_url"]
    
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
        fields  = ["id"]

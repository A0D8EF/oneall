from django import forms
from .models import Chat, ChatGroup

from django.core.exceptions import ValidationError

class ChatForm(forms.ModelForm):

    class Meta:
        model   = Chat
        fields  = ["group", "user", "message"]


class ChatGroupForm(forms.ModelForm):

    class Meta:
        model   = ChatGroup
        fields  = ["member"]
    
    def clean(self):
        data    = self.cleaned_data
        members = data["member"]

        if len(members) > 2:
            raise ValidationError("メンバーは2人まで")
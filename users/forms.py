from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import CustomUser

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model   = CustomUser
        fields  = ["username", "email", "handle_name"]


class CustomUserEditForm(forms.ModelForm):
    class Meta:
        model   = CustomUser
        fields  = [ "handle_name", "icon", "introduction" ]
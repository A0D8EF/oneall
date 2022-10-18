from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from .forms import CustomUserEditForm

class IndexView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, "users/index.html")
    

    def post(self, request, *args, **kwargs):
        
        form    = CustomUserEditForm(request.POST, request.FILES, instance=request.user)

        if form.is_valid():
            print("ユーザー情報編集完了")
            form.save()
        
        return redirect("users:index")


index = IndexView.as_view()

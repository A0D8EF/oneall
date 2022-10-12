from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, "oneall/index.html", context)

index = IndexView.as_view()
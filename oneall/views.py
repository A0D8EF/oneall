from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from news.models import News
from textbook.models import Textbook

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context                 = {}
        context["newses"]       = News.objects.all().order_by("-dt")[:5]
        context["textbooks"]    = Textbook.objects.all().order_by("top_order", "-dt")

        return render(request, "oneall/index.html", context)

index = IndexView.as_view()
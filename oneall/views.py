from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.core.paginator import Paginator

from news.models import Category, News

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context     = {}

        newses      = News.objects.all().order_by("-dt")
        paginator   = Paginator(newses, 5)

        context["newses"]   = paginator.get_page(1)

        return render(request, "oneall/index.html", context)

index = IndexView.as_view()
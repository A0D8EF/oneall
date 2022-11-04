from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.views import View
from rest_framework.views import APIView as View

from django.db.models import Q
from django.core.paginator import Paginator

from .models import Category, News
from .forms import NewsForm, CategorySearchForm, CategoryForm

from django.contrib import messages

from django.http import HttpResponseNotFound
from django.http.response import JsonResponse
from django.template.loader import render_to_string

class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context = {}
        query   = Q()

        if "search" in request.GET:
            search      = request.GET["search"]
            raw_words   = search.replace("　"," ").split(" ")
            words       = [ w for w in raw_words if w != ""]

            for w in words:
                query &= Q(title__contains=w)
        
        form    = CategorySearchForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            # ForeignKeyをバリデーション、clean()して得られる値は、紐づいているモデルオブジェクト。
            query   &= Q(category=cleaned["category"].id)

        newses      = News.objects.filter(query).order_by("-dt")
        paginator   = Paginator(newses, 10)

        if "page" in request.GET:
            context["newses"]   = paginator.get_page(request.GET["page"])
        else:
            context["newses"]   = paginator.get_page(1)
        
        # context["newses"]       = News.objects.filter(query).order_by("-dt")
        context["categories"]   = Category.objects.all()

        return render(request, "news/index.html", context)

    def post(self, request, *args, **kwargs):

        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = NewsForm(copied)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("news:index")

        print("バリデーションOK")
        form.save()

        return redirect("news:index")

index = IndexView.as_view()


class NewsDetailView(LoginRequiredMixin,View):
    def get(self, request, pk, *args, **kwargs):
        context         = {}

        news    = News.objects.filter(id=pk).first()
        if not news:

            # return redirect("news:index")
            return HttpResponseNotFound(render_to_string("oneall/notfound.html"))
        
        context["news"] = news
        if request.user.is_teacher:
            context["categories"]   = Category.objects.all()

        return render(request, "news/detail.html", context)
    

    def delete(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        news    = News.objects.filter(id=pk).first()
        if news:
            news.delete()
            data["error"] = False

        return JsonResponse(data)
    

    def put(self, request, pk, *args, **kwargs):
        
        data    = { "error": True }

        news            = News.objects.filter(id=pk).first()
        copied          = request.POST.copy()
        copied["user"]  = request.user.id

        form    = NewsForm(copied, instance=news)

        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return JsonResponse(data)
        
        form.save()
        data["error"]   = False

        return JsonResponse(data)
    

detail = NewsDetailView.as_view()


class AddCategoryView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        categories  = Category.objects.all()
        copied      = request.POST.copy()
        
        form    = CategoryForm(copied)
        if not form.is_valid():
            print(form.errors)
            
            values  = form.errors.get_json_data().values()
            for value in values:
                for v in value:
                    messages.error(request, v["message"])
            
            return redirect("news:index")
        
        print("バリデーションOK")
        form.save()

        return redirect("news:index")


add_category = AddCategoryView.as_view()

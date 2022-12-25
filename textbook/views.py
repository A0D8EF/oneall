from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q
from django.core.paginator import Paginator

from .models import MajorCategory, MinorCategory, Textbook
from .forms import TextbookForm, MajorCategoryForm, MinorCategoryForm
from .forms import MajorCategorySearchForm, MinorCategorySearchForm

from . import scraping

from django.contrib import messages

from django.http.response import JsonResponse
from django.template.loader import render_to_string


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        query   = Q()
        
        if "search" in request.GET:
            search      = request.GET["search"]
            raw_words   = search.replace("　"," ").split(" ")
            words       = [ w for w in raw_words if w != ""]

            for w in words:
                query &= Q(title__contains=w)
        
        form    = MajorCategorySearchForm(request.GET)        
        if form.is_valid():
            cleaned = form.clean()
            query   &= Q(major_category=cleaned["major_category"].id)
        
        form    = MinorCategorySearchForm(request.GET)
        if form.is_valid():
            cleaned = form.clean()
            query   &= Q(minor_category=cleaned["minor_category"].id)
        
        textbooks   = Textbook.objects.filter(query).order_by("top_order", "-dt")
        paginator   = Paginator(textbooks, 10)

        if "page" in request.GET:
            context["textbooks"]    = paginator.get_page(request.GET["page"])
        else:
            context["textbooks"]    = paginator.get_page(1)
        
        context["major_categories"] = MajorCategory.objects.all().order_by("order")
        context["minor_categories"] = MinorCategory.objects.all().order_by("order")

        return render(request, "textbook/index.html", context)

    def post(self, request, *args, **kwargs):
        copied              = request.POST.copy()
        copied["user"]      = request.user.id

        print(copied)

        if "is_youtube" in copied:
            copied["thumbnail_url"] = scraping.youtube_thumbnail(copied)

        form                = TextbookForm(copied, request.FILES)
        if not form.is_valid():
            print("バリデーションNG")
            print(form.errors)
            return redirect("textbook:index")
        
        form.save()

        return redirect("textbook:index")


index = IndexView.as_view()


class AddTextbookView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        data    = { "error": True }

        # form    = MajorCategoryForm(request.GET)

        # if not form.is_valid():
        #     print(form.errors)
        #     return JsonResponse(data)
        
        # cleaned     = form.clean()
        
        context     = {}
        context["minor_categories"] = MinorCategory.objects.filter(parent=request.GET["major_category"])

        data["error"]   = False
        data["content"] = render_to_string("textbook/minor_category.html", context, request)

        return JsonResponse(data)


add = AddTextbookView.as_view()


class AddMajorCategoryView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        major_categories    = MajorCategory.objects.all()
        copied              = request.POST.copy()

        form    = MajorCategoryForm(copied)
        if not form.is_valid():
            print(form.errors)
            
            values  = form.errors.get_json_data().values()
            for value in values:
                for v in value:
                    messages.error(request, v["message"])
            
            return redirect("textbook:index")
        
        print("バリデーションOK")
        form.save()

        return redirect("textbook:index")


add_major_category = AddMajorCategoryView.as_view()


class AddMinorCategoryView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):

        minor_categories    = MinorCategory.objects.all()
        copied              = request.POST.copy()

        form    = MinorCategoryForm(copied)
        if not form.is_valid():
            print(form.errors)
            
            # values  = form.errors.get_json_data().values()
            # for value in values:
            #     for v in value:
            #         messages.error(request, v["message"])
            
            return redirect("textbook:index")
        
        print("バリデーションOK")
        form.save()

        return redirect("textbook:index")



add_minor_category = AddMinorCategoryView.as_view()

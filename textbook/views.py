from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

from django.db.models import Q
from django.core.paginator import Paginator

from .models import MajorCategory, MinorCategory, Textbook
from .forms import TextbookForm, MajorCategoryForm

from django.http.response import JsonResponse
from django.template.loader import render_to_string


class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        
        textbooks   = Textbook.objects.all().order_by("-dt")[:5]
        paginator   = Paginator(textbooks, 10)

        if "page" in request.GET:
            context["textbooks"]    = paginator.get_page(request.GET["page"])
        else:
            context["textbooks"]    = paginator.get_page(1)
        
        context["major_categories"] = MajorCategory.objects.all()
        context["minor_categories"] = MinorCategory.objects.all()

        return render(request, "textbook/index.html", context)

    def post(self, request, *args, **kwargs):
        copied              = request.POST.copy()
        copied["user"]      = request.user.id

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
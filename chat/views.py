from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from .models import Chat, ChatGroup
from .forms import ChatForm

from django.http.response import JsonResponse
from django.template.loader import render_to_string

import operator


class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context         = {}

        chat_groups     = ChatGroup.objects.filter(member=request.user.id)
        ordered         = sorted(chat_groups, key=operator.methodcaller("latest_message"), reverse=True)

        context["chat_groups"]  = ordered

        """
        context["chat_groups"]  = ChatGroup.objects.filter(member=request.user.id).order_by("-dt")
        """
        return render(request, "chat/index.html", context)

index = IndexView.as_view()


class ChatMessageView(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):
        data    = {"error": True}
        context = {}

        context["chat_group"]   = ChatGroup.objects.filter(id=pk).first()

        data["error"]   = False
        data["content"] = render_to_string("chat/chat_area.html", context, request)

        return JsonResponse(data)


    def post(self, request, pk, *args, **kwargs):
        data    = {"error": True}
        context = {}

        copied          = request.POST.copy()
        copied["group"] = pk
        copied["user"]  = request.user.id
        
        form    = ChatForm(copied)
        if not form.is_valid():
            return JsonResponse(data)
        
        form.save()

        context["chat_group"]   = ChatGroup.objects.filter(id=pk).first()

        data["error"]   = False
        data["content"] = render_to_string("chat/chat_area.html", context, request)

        return JsonResponse(data)


chat_message = ChatMessageView.as_view()


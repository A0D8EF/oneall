from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


from .models import Chat, ChatGroup
from .forms import ChatForm

class IndexView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        context         = {}

        context["chat_groups"]  = ChatGroup.objects.filter(member=request.user.id).order_by("-dt")

        return render(request, "chat/index.html", context)

    def post(self, request, *args, **kwargs):
        

        return redirect("chat:index")
    

index = IndexView.as_view()

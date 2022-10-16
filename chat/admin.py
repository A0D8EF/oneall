from django.contrib import admin

from .models import Chat, ChatGroup
from .forms import ChatGroupForm

class ChatGroupAdmin(admin.ModelAdmin):

    form = ChatGroupForm

    list_display    = ["id", "dt", "members"]

    def members(self, obj):
        if obj.member:
            member_list = [ member.handle_name for member in obj.member.all() ]

            return member_list


admin.site.register(Chat)
admin.site.register(ChatGroup, ChatGroupAdmin)

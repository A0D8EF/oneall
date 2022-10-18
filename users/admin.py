from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('handle_name', 'email', "icon", "introduction", "is_teacher", "is_student")}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'handle_name', 'email', "is_teacher", "is_student"),
        }),
    )

    list_display = ('username', 'email', 'handle_name', 'is_staff', "is_teacher", "is_student")
    search_fields = ('username', 'handle_name', 'email')

admin.site.register(CustomUser, CustomUserAdmin)


from django.contrib import admin
from .models import MajorCategory, MinorCategory, Textbook
from .forms import TextbookAdminForm

class MajorCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "name"]

class MinorCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "name", "parent"]

class TextbookAdmin(admin.ModelAdmin):
    list_display = ["id", "dt", "is_top", "title", "major_category", "minor_category"]
    form    = TextbookAdminForm

admin.site.register(MajorCategory, MajorCategoryAdmin)
admin.site.register(MinorCategory, MinorCategoryAdmin)
admin.site.register(Textbook, TextbookAdmin)

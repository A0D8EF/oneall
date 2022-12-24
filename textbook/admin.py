from django.contrib import admin
from .models import MajorCategory, MinorCategory, Textbook

class MajorCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "name"]

class MinorCategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "order", "name", "parent"]

class TextbookAdmin(admin.ModelAdmin):
    list_display = ["id", "dt", "thumbnail", "title", "major_category", "minor_category"]

admin.site.register(MajorCategory, MajorCategoryAdmin)
admin.site.register(MinorCategory, MinorCategoryAdmin)
admin.site.register(Textbook, TextbookAdmin)

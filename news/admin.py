from django.contrib import admin
from .models import Category, News

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "dt", "title", "category"]

admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)

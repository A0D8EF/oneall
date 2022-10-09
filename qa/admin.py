from django.contrib import admin
from .models import Tag, Question

class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "dt", "title"]

admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)

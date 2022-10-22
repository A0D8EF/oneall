from django.contrib import admin
from .models import Tag, Question, Answer

class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "dt", "title"]
    
class AnswerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "dt", "target"]

admin.site.register(Tag, TagAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

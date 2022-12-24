from django.contrib import admin
from .models import AC, Question, ABC, Interview, Contract

class ACAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "ac_date", "c_name", "c_is_ac_active"]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "q_date", "ac", "c_is_question_active"]

class ABCAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "abc_date", "question", "c_is_abc_active"]

class InterviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "interview_date", "abc", "c_is_interview_active"]

class ContractAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "contract_date", "interview"]

admin.site.register(AC, ACAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ABC, ABCAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Contract, ContractAdmin)
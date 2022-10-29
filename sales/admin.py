from django.contrib import admin
from .models import AC, Question, ABC, Interview, Contract

class ACAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "ac_date", "c_name"]

class QuestionAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "q_date", "ac"]

class ABCAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "abc_date", "question"]

class InterviewAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "interview_date", "abc"]

class ContractAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "contract_date", "interview"]

admin.site.register(AC, ACAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(ABC, ABCAdmin)
admin.site.register(Interview, InterviewAdmin)
admin.site.register(Contract, ContractAdmin)
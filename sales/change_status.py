from .models import AC, Question, ABC, Interview

import datetime
from django.utils import timezone as tz

def change_inactive(request, today):
    acs     = AC.objects.filter(user=request.user.id)
    for ac in acs:
        if ac.c_is_ac_active and (ac.ac_date + tz.timedelta(days=21) < today):
            ac.c_is_ac_active = False
            ac.save()

    questions   = Question.objects.filter(user=request.user.id)
    for question in questions:
        if question.c_is_question_active and (question.q_date + tz.timedelta(days=21) < datetime.date.today()):
            question.c_is_question_active = False
            question.save()
    
    abcs    = ABC.objects.filter(user=request.user.id)
    for abc in abcs:
        if abc.c_is_abc_active and (abc.abc_date + tz.timedelta(days=21) < today):
            abc.c_is_abc_active = False
            abc.save()

    interviews  = Interview.objects.filter(user=request.user.id)
    for interview in interviews:
        if interview.c_is_interview_active and (interview.interview_date + tz.timedelta(days=21) < today):
            interview.c_is_interview_active = False
            interview.save()
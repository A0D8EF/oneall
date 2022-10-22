from django.urls import path
from . import views

app_name = "qa"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:pk>/", views.detail, name="detail"),
    path("question_good/<int:pk>/", views.question_good, name="question_good"),
    path("answer_good/<int:q_id>/<int:a_id>/", views.answer_good, name="answer_good"),
]

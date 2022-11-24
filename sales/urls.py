from django.urls import path
from . import views

app_name = "sales"
urlpatterns = [
    path("", views.index, name="index"),
    path("ac/<int:pk>/", views.ac_detail, name="ac_detail"),
    path("q/<int:pk>/", views.q_detail, name="q_detail"),
    path("abc/<int:pk>/", views.abc_detail, name="abc_detail"),
    path("interview/<int:pk>/", views.interview_detail, name="interview_detail"),
    path("contract/<int:pk>/", views.contract_detail, name="contract_detail"),
]

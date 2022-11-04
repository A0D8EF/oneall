from django.urls import path
from . import views

app_name = "textbook"
urlpatterns = [
    path("", views.index, name="index"),
    path("add/", views.add, name="add"),
    path("add_major_category/", views.add_major_category, name="add_major_category"),
    path("add_minor_category/", views.add_minor_category, name="add_minor_category"),
]

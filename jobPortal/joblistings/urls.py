from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("joblistings/", views.index, name="index"),
    path("formsuccess/", views.success, name="success"),
]
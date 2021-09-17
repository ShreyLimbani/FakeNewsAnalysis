from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("index", views.index),
    path("searchnews", views.searchnews, name="searchnews"),
    path("analytics", views.analytics, name="analytics"),
    path("about", views.about, name="about"),
]
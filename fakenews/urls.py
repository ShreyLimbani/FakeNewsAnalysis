from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("index", views.index),
    path("searchresults", views.searchresults, name="searchresults"),
    path("searchnews", views.searchnews, name="searchnews"),
    path("searchnewsresults", views.searchnewsresults, name="searchnewsresults"),
    path("analytics", views.analytics, name="analytics"),
    path("about", views.about, name="about"),
]
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "fakenews/index.html")

def searchnews(request):
    return render(request, "fakenews/searchnews.html")

def analytics(request):
    return render(request, "fakenews/analytics.html")

def about(request):
    return render(request, "fakenews/about.html")
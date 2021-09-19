from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    return render(request, "fakenews/index.html")

def searchresults(request):
    search = request.GET['search']
    return render(request, "fakenews/searchresults.html",context={'search':search})

def searchnews(request):
    return render(request, "fakenews/searchnews.html")

def searchnewsresults(request):
    return render(request, "fakenews/searchnewsresults.html")

def analytics(request):
    return render(request, "fakenews/analytics.html")

def about(request):
    return render(request, "fakenews/about.html")
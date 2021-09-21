from django.http import response
from django.shortcuts import redirect, render
import requests
import json
from FakeNewsAnalysis.settings import NEWS_API_KEY

api_url = 'https://newsapi.org/v2/everything'
params={
    'q':'',
    'language':'en',
    'sortBy':'publishedAt',
    'pageSize': 12
}

# Create your views here.
def index(request):
    return render(request, "fakenews/index.html")

def searchresults(request):
    search = request.GET['search']
    return render(request, "fakenews/searchresults.html",context={'search':search, 'form_action':'searchresults'})

def searchnews(request):
    return render(request, "fakenews/searchnews.html")

def searchnewsresults(request):
    search = request.GET['search']
    try:
        current_page = int(request.GET['page'])
    except KeyError:
        current_page = 1

    params['q'] = search
    params['page'] = current_page

    news_response = requests.get(api_url,params=params, headers={"Authorization":NEWS_API_KEY})
    if news_response.status_code == 200:
        news_articles = news_response.json()
    else:
        news_articles = news_response.json()['message']
    
    total_articles = min(100,news_articles['totalResults'])
    if total_articles%12!=0:
        total_articles = total_articles - (total_articles%12)
    articles = sorted(news_articles['articles'], key=lambda item : item['publishedAt'], reverse=True)

    return render(
        request, "fakenews/searchnewsresults.html",
        context={
            'articles':articles,'search':search, 'form_action':'searchnewsresults', 'total_pages':max(1,(total_articles//12)),
            'current_page':current_page, 'prev':current_page-1, 'next':current_page+1,
        }
    )

def analytics(request):
    return render(request, "fakenews/analytics.html")

def about(request):
    return render(request, "fakenews/about.html")
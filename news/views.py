from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    news = models.News.objects.all()
    context = {
        'news' : news
    }
    return render(request,'news/index.html',context)
def single(request,news_id):
    new = models.News.objects.get(pk = news_id)
    context = {
        'new' : new
    }

    return render(request,'news/single.html',context)
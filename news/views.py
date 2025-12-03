from django.shortcuts import render, get_object_or_404
from .models import News

def news_list(request):
    news_list = News.objects.order_by('-created_at')
    return render(request, 'news/list.html', {'news_list': news_list})

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'news/detail.html', {'news': news})

def index(request):
    recent_news = News.objects.order_by('-published_at')[:4]
    return render(request, 'news/index.html', {
        'recent_news': recent_news,
    })

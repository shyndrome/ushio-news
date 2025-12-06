from django.http import JsonResponse
from .models import News

def api_news_list(request):
    items = News.objects.order_by('-date')
    data = []
    for n in items:
        data.append({
            "title": n.title,
            "slug": n.slug,
            "date": n.date.strftime("%Y.%m.%d"),
        })
    return JsonResponse(data, safe=False)


def api_news_detail(request, slug):
    n = News.objects.get(slug=slug)
    images = [img.image.url for img in n.images.all()]

    return JsonResponse({
        "title": n.title,
        "date": n.date.strftime("%Y.%m.%d"),
        "content": n.content,
        "images": images,
    })

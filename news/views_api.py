from django.http import JsonResponse
from .models import News

def api_news_list(request):
    # すべての記事を取得
    items = News.objects.order_by('-date')
    data = []
    
    for n in items:
        # 各記事に紐付く画像のURLリストを作成
        images = [img.image.url for img in n.images.all()]
        
        data.append({
            "title": n.title,
            "slug": n.slug,
            "date": n.date.strftime("%Y.%m.%d"),
            "content": n.content,  # ← これを追加！
            "images": images,      # ← これを追加！
        })
    
    return JsonResponse(data, safe=False)

# 詳細用（もし個別のページを作るなら使います）
def api_news_detail(request, slug):
    try:
        n = News.objects.get(slug=slug)
        images = [img.image.url for img in n.images.all()]
        return JsonResponse({
            "title": n.title,
            "date": n.date.strftime("%Y.%m.%d"),
            "content": n.content,
            "images": images,
        })
    except News.DoesNotExist:
        return JsonResponse({"error": "Not found"}, status=404)
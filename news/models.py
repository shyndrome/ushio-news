from django.db import models
from django.utils.text import slugify
import uuid

class News(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    content = models.TextField()   # 今の文章すべてここに入る
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"  # ← これで複数形も News のまま！

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.date}-{self.title}-{uuid.uuid4().hex[:6]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class NewsImage(models.Model):
    news = models.ForeignKey(News, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_images/')
    caption = models.TextField(blank=True)

    def __str__(self):
        return f"Image for {self.news.title}"

from django.db import models
from django.utils.text import slugify
import uuid

class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

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
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="news_images/")

    class Meta:
        verbose_name = "News Image"
        verbose_name_plural = "News Images"

    def __str__(self):
        return f"Image for {self.news.title}"

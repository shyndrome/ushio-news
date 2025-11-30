from django.contrib import admin
from .models import News, NewsImage

class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    inlines = [NewsImageInline]

admin.site.register(News, NewsAdmin)

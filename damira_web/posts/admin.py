from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')  # Поля, которые будут отображаться в списке
    search_fields = ('title', 'description')  # Поля, по которым можно искать

admin.site.register(Article, ArticleAdmin)
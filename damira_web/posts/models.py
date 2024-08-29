from django.db import models

from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    urlName = models.CharField(max_length=100, verbose_name='Nazwa url', unique=True)
    title = models.CharField(max_length=200, verbose_name='Nagłówek')
    description = models.TextField(verbose_name='Opis strony')
    content = RichTextField(verbose_name='Kontent')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Stworzono')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Zaktualizowano')

    class Meta():
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'

    def __str__(self):
        return self.title
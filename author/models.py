from django.db import models
from datetime import *

class Blogpost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name="Пост"
        verbose_name_plural="Посты"




class Item2(models.Model):
    name = models.CharField(max_length=225, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена')
    image = models.CharField(max_length=225, verbose_name='Ссылка на картинку')
    alias = models.SlugField(verbose_name='Alias товара')

    class Meta:
        verbose_name="Товар"
        verbose_name_plural="Товары"

    def __unicode__(self):
        return self.name


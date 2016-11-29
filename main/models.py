from django.db import models


from django.contrib.comments.moderation import CommentModerator, moderator
from django.core.urlresolvers import reverse



class Books(models.Model):
  name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Название")
  author = models.CharField(max_length = 30, unique = False, db_index = True, verbose_name = "Автор")
  theme = models.CharField(max_length = 100, unique = False, db_index = True, verbose_name = "Тематика")
  edition = models.CharField(max_length = 100, unique = False, db_index = True, verbose_name = "Вид издания")
  isbn = models.CharField(max_length = 30, unique = True, db_index = True, verbose_name = "ISBN")
  tags = models.CharField(max_length = 100, unique = False, db_index = True, verbose_name = "Теги")
  holder = models.CharField(max_length = 100, unique = False, db_index = True, verbose_name = "Правообладатель")
  release = models.DateField(db_index = True, verbose_name = "Год выпуска")
  form = models.CharField(max_length = 15, unique = False, db_index = True, verbose_name = "Формат")
  number = models.CharField(max_length = 30, unique = False, db_index = True, verbose_name = "Объем")
  image = models.ImageField(upload_to = "books/list", verbose_name = "Основное изображение")
  about = models.TextField(verbose_name = "От автора")
  alias = models.SlugField(verbose_name='Alias книги')
  def __unicode__(self):
        return self.name
  class Meta:
        verbose_name="Книга"
        verbose_name_plural="Книги"

class Guestbook(models.Model):
  books = models.ForeignKey(Books, verbose_name = "Книга")
  user = models.CharField(max_length = 20, verbose_name = "Пользователь")
  posted = models.DateTimeField(auto_now_add = True, db_index = True, verbose_name = "Опубликовано")
  content = models.TextField(verbose_name = "Отзыв")


  class Meta:
        verbose_name="Отзыв"
        verbose_name_plural="Отзывы"



class Country(models.Model):
  name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Название")
  def __unicode__(self):
        return self.name
  class Meta:
        verbose_name="Страна доставки"
        verbose_name_plural="Страны доставки"

class Order(models.Model):
  books = models.ForeignKey(Books, verbose_name = "Книга")
  qty = models.PositiveIntegerField(default=1, max_length = 7, unique = False, db_index = True, verbose_name = "Количество экземпляров")
  post_index = models.PositiveIntegerField(max_length = 6, unique = False, db_index = True, verbose_name = "Почтовый индекс")
  country = models.ForeignKey(Country, verbose_name = "Страна")
  address = models.CharField(max_length = 100, unique = False, db_index = True, verbose_name = "Адрес доставки")
  fio = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Ваше ФИО")
  mail = models.EmailField(unique = False, db_index = True, verbose_name = "E-mail для связи")
  comment = models.TextField(verbose_name = "Комментарий")

  class Meta:
        verbose_name="Заказ"
        verbose_name_plural="Заказы"



from django.db import models

class MailList(models.Model):
  username = models.CharField(max_length = 50, verbose_name = "Введите ваше имя")
  email = models.EmailField(unique = True, verbose_name = "E-mail адрес")
  text = models.TextField(verbose_name = "Введите текст вашего сообщения")

  class Meta:
    verbose_name = "Сообщение для Юрия Павловича"
    verbose_name_plural = "Сообщения для Юрия Павловича"
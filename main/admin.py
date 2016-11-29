from django.contrib import admin

from main.models import Books
from main.models import Guestbook, Order, Country


class BooksAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
admin.site.register(Books, BooksAdmin)



class GuestbookAdmin(admin.ModelAdmin):
    list_display = ('user', 'posted', 'content', 'books')
admin.site.register(Guestbook, GuestbookAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('books', 'qty', 'fio', 'mail')
admin.site.register(Order, OrderAdmin)

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
admin.site.register(Country, CountryAdmin)
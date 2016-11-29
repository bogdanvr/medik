from django.contrib import admin



from author.models import Blogpost
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'timestamp')

admin.site.register(Blogpost, BlogpostAdmin)


from author.models import Item2
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

admin.site.register(Item2, ItemAdmin)

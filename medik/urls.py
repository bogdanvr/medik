from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from contacts.views import ContactsView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'medik.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^', include('main.urls')),
    url(r'^archive/', include('author.urls')),
    url(r'^author/', include('author.urls')),
    url(r'^item2/(?P<alias>[^/]+)', 'author.views.item2'),
    url(r'^contacts/', ContactsView.as_view(), name = "contacts"),
    url(r'^news/', include('news.urls')),
    url(r'^booksdetail/(?P<book_id>\d+)/$', 'main.views.booksdetail', name = "booksdetail1"),
    url(r'^booksdetail/addcomment/(?P<book_id>\d+)/$', 'main.views.addcomment'),









)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

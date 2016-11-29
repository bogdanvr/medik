from django.conf.urls import patterns, url
from author.views import AuthorView



import author.views

urlpatterns = patterns('',



  url(r'^$', author.views.archive, name = "archive"),
  url(r'^author/$', AuthorView.as_view(), name = "authorview"),
)
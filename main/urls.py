from django.conf.urls import patterns, url

from main.views import MainPageView, OrderView, ReadView, SupportView
import main.views

urlpatterns = patterns('',
  url(r'^$', MainPageView.as_view(), name = "main"),
  url(r'^booksdetail/pdf/$', main.views.someview, name = "pdfu"),
  url(r'^booksdetail/time/$', "main.views.timeview", name = "timeu"),
  url(r'^booksdetail/order/$', OrderView.as_view(), name = "orderview"),
  url(r'^booksdetail/read/$', ReadView.as_view(), name = "readview"),
  url(r'^booksdetail/support/$', SupportView.as_view(), name = "supportview"),

)

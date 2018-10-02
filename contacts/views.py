# -*- coding: utf-8 -*-
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import ContextMixin
#from generic.mixins import CategoryListMixin
from contacts.models import MailList



class CategoryListMixin(ContextMixin):
  def get_context_data(self, **kwargs):
    context = super(CategoryListMixin, self).get_context_data(**kwargs)
    context["current_url"] = self.request.path

    return context
    
class PageNumberMixin(CategoryListMixin):
  def get_context_data(self, **kwargs):
    context = super(PageNumberMixin, self).get_context_data(**kwargs)
    try:
      context["pn"] = self.request.GET["page"]
    except KeyError:
      context["pn"] = "1"
    return context



class ContactsView(SuccessMessageMixin, CreateView, CategoryListMixin):
  model = MailList
  template_name = "contacts.html"
  success_url = reverse_lazy("contacts")
  success_message = "Ваше сообщение успешно отправлено"
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response


from main.views import PageNumberView
from django.views.generic.list import ListView
from main.models import *

from datetime import datetime
from author.models import *
from contacts.views import CategoryListMixin
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from django.views.generic.base import TemplateView

def archive(request):
    tovars = Item2.objects.all()

    context = {'title': 'Hello world', 'tovars': tovars}
    return HttpResponse(render_to_string('author2.html', context))


def item2(request, alias):
    try:
        tovar = Item2.objects.get(alias=alias)
    except:
        raise Http404('Объект не найден')
    context = { 'tovar': tovar}
    return HttpResponse(render_to_string('item.html', context))

class AuthorView(TemplateView, CategoryListMixin):
    template_name = "author.html"

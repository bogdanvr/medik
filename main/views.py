from django.shortcuts import render

from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from generic.controllers import PageNumberView
from django.views.generic.list import ListView
from main.models import Books
from main.forms import BookForm

from django.views.generic.dates import ArchiveIndexView
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template.loader import render_to_string
from django.shortcuts import render_to_response, redirect
from main.forms import BookForm, OrderForm
from django.core.context_processors import csrf
from main.models import Guestbook, Order
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from reportlab.lib.units import cm
import datetime
from django.contrib import messages




class MainPageView(ListView, CategoryListMixin):
  template_name = "mainpage.html"
  model = Books
  context_object_name = 'main_books'
  allow_empty = True
  allow_future = True




def booksdetail(request, book_id):
    book_form = BookForm
    args = {}
    args.update(csrf(request))
    args['name_context'] = Books.objects.get(id=book_id)
    args['comments'] = Guestbook.objects.filter(books_id=book_id)
    args['form'] = book_form
    args['num_comments'] = Guestbook.objects.filter(books_id=book_id).count()
    return render_to_response('booksdetail.html', args)


def addcomment(request, book_id):
    if request.POST:
        form = BookForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.books = Books.objects.get(id=book_id)
            form.save()
    return redirect('/booksdetail/%s' % book_id)

def someview(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the BytesIO object as its "file."
    p = canvas.Canvas(buffer)
    p.setLineWidth(.3)
    p.setFont('Helvetica', 12)

    p.drawString(30,750,'OFFICIAL COMMUNIQUE')
    p.drawString(30,735,'OF ACME INDUSTRIES')
    p.drawString(500,750,"12/12/2010")
    p.line(480,747,580,747)

    p.drawString(275,725,'AMOUNT OWED:')
    p.drawString(500,725,"$1,000.00")
    p.line(378,723,580,723)

    p.drawString(30,703,'RECEIVED BY:')
    p.line(120,700,580,700)
    p.drawString(120,703,"JOHN DOE")
    p.save()

    # Get the value of the BytesIO buffer and write it to the response.
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def timeview(request):
    now = datetime.datetime.now()
    html = "<html><body>Сейчас %s.</body></html>" % now
    return HttpResponse(html)

class OrderView(TemplateView):
    model = Order
    template_name = "order.html"
    form = None
    def get(self, request, *args, **kwargs):
        self.form = OrderForm()
        return super(OrderView, self).get(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context["form"] = self.form
        return context
    def post(self, request, *args, **kwargs):
        self.form = OrderForm(request.POST)
        if self.form.is_valid():
            if self.form.cleaned_data["honeypot"] == "":
                if self.form['qty'] > 0:
                    self.form.save()
                    messages.add_message(request, messages.SUCCESS, "Заказ успешно отправлен.")
                return redirect("main")
        else:
            return super(OrderView, self).get(request, *args, **kwargs)

class ReadView(TemplateView):
    template_name = "read.html"


class SupportView(TemplateView):
    template_name = "support.html"
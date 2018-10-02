# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm, TextInput, Textarea

from main.models import Guestbook, Order, Books, Country

class BookForm(forms.ModelForm):
    class Meta:
        fields = ['user', 'content']
        model = Guestbook

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['books', 'qty','fio', 'mail','country','post_index', 'address','comment' ]
        widgets = {'post_index':TextInput(attrs={'cols': 80, 'rows': 20}),}
    honeypot = forms.CharField(required=False, label='Ловушка для спамеров')
    def clean_email(self):
        data = self.cleaned_data['qty']
        if data > 0:
            raise forms.ValidationError("Пожалуйста используйте fred@mail.ru адрес")
        return data

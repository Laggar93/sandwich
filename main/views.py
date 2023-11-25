from django.http import HttpResponseNotFound
from django.shortcuts import render

from sandwich.sendform import send_excursion
from .forms import main_form
from .models import *


def main_view(request):
    link_kg = '/ky/'
    link_kz = '/kk/'
    link_ru = '/ru/'
    link_en = '/en/'

    content = {
        'seo': seo.objects.first(),
        'about': about.objects.first(),
        'product': product.objects.first(),
        'product_items': product_items.objects.all(),
        'cooperation': cooperation.objects.first(),
        'vacancy': vacancy.objects.first(),
        'contacts': contacts.objects.first(),
        'intro': intro.objects.first(),
        'compound': compound.objects.first(),
        'general': general.objects.first(),
        'form': main_form,
        'link_kg': link_kg,
        'link_kz': link_kz,
        'link_ru': link_ru,
        'link_en': link_en,
    }

    return render(request, 'index.html', content)


def form_view(request):
    if request.is_ajax() and request.POST:
        form = main_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            department = form.cleaned_data['message']
            return send_excursion(name, phone, date, department)
    return HttpResponseNotFound("")
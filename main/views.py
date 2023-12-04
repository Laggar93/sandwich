from django.http import HttpResponseNotFound, HttpResponse
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
        'departments': departments.objects.all(),
        'cooperation': cooperation.objects.first(),
        'vacancy': vacancy.objects.first(),
        'contacts': contacts.objects.first(),
        'intro': intro.objects.first(),
        'compound': compound.objects.first(),
        'general': general.objects.first(),
        'form_translation': form_translation.objects.first(),
        'form': main_form,
        'link_kg': link_kg,
        'link_kz': link_kz,
        'link_ru': link_ru,
        'link_en': link_en,
    }

    return render(request, 'index.html', content)


def form_view(request):
    success_message = None
    error_message = None
    if request.method == 'POST':
        form = main_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            department = form.cleaned_data['department']  # Ensure the department is retrieved correctly
            emp = model_form.objects.create(name=name, phone=phone, date=date, department=department)
            emp.save()
            success_message = general.objects.first().success_form
            return HttpResponse("OK")
        else:
            # Handling invalid form data
            error_message = general.objects.first().error_form
            return HttpResponse("Error")
    form = main_form()
    return HttpResponse("haha")

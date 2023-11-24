from django.shortcuts import render
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
        'cooperation': cooperation.objects.first(),
        'vacancy': vacancy.objects.first(),
        'contacts': contacts.objects.first(),
        'intro': intro.objects.first(),
        'compound': compound.objects.first(),
        'general': general.objects.first(),
        'link_kg': link_kg,
        'link_kz': link_kz,
        'link_ru': link_ru,
        'link_en': link_en,
    }

    return render(request, 'index.html', content)
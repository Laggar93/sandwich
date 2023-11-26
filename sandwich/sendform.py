import re
from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
# from vector.config import send_mail


def send_excursion(name, phone, date, department):
    name = re.sub('<[^<]+?>', '', name)
    phone = re.sub('<[^<]+?>', '', phone)
    date = date
    department = department
    body = f'Имя - {name}\n Телефон - {phone}\n Дата - {date} - Отдел - {department}'
    send_msg = EmailMessage('Сообщение с сайта', body, settings.EMAIL_HOST_USER, ['ulikfr1d@gmail.com'])
    send_msg.content_subtype = "html"
    send_msg.send()
    if send_msg.send() == 1:
        return HttpResponse(f'<div class="form__success">{1}</div>')
    else:
        return HttpResponse(f'<div class="form__error">{0}</div>')
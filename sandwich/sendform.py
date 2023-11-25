import re
from django.shortcuts import HttpResponse
from django.core.mail import EmailMessage
from django.conf import settings
# from vector.config import send_mail


def send_excursion(name, date, phone, department):
    name = re.sub('<[^<]+?>', '', name)
    phone = re.sub('<[^<]+?>', '', phone)
    date = re.sub('<[^<]+?>', '', date)
    department = re.sub('<[^<]+?>', '', department)
    body = '<p>Имя: ' + name + '</p><p>Телефон: <a href="tel:' + phone + '">' + date + '</a></p><p>Электронная почта: <a href="mailto:' + department + '">' + '</p>'
    send_msg = EmailMessage('Сообщение с сайта', body, settings.EMAIL_HOST_USER, ['ulikfr1d@gmail.com'])
    send_msg.content_subtype = "html"
    send_msg.send()
    if send_msg.send() == 1:
        return HttpResponse(f'<div class="form__success">{1}</div>')
    else:
        return HttpResponse(f'<div class="form__error">{0}</div>')
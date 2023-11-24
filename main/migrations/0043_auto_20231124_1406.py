# Generated by Django 3.2.8 on 2023-11-24 14:06

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20231124_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperation',
            name='discuss_list_en',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Список из "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_list_kk',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Список из "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_list_ky',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Список из "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_list_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Список из "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='discuss_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Обсудим с вами"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='menu_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='menu_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='menu_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='menu_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='posm_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Дарим POSM материалы"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='posm_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Дарим POSM материалы"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='posm_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Дарим POSM материалы"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='posm_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Дарим POSM материалы"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_button_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Позвонить в отдел продаж"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_button_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Позвонить в отдел продаж"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_button_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Позвонить в отдел продаж"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_button_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Позвонить в отдел продаж"'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_phone_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Телефон отдела продаж'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_phone_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Телефон отдела продаж'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_phone_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Телефон отдела продаж'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='sale_phone_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Телефон отдела продаж'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='title_en',
            field=models.TextField(null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='title_kk',
            field=models.TextField(null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='title_ky',
            field=models.TextField(null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='cooperation',
            name='title_ru',
            field=models.TextField(null=True, verbose_name='Заголовок'),
        ),
    ]

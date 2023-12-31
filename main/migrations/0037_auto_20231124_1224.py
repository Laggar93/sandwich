# Generated by Django 3.2.8 on 2023-11-24 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_auto_20231124_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='menu_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='about',
            name='menu_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='about',
            name='menu_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='about',
            name='menu_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_en',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='about',
            name='text_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Текст'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок раздела'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок раздела'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок раздела'),
        ),
        migrations.AddField(
            model_name='about',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок раздела'),
        ),
    ]

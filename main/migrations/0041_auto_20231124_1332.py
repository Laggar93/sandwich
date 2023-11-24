# Generated by Django 3.2.8 on 2023-11-24 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_product_menu_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_kk',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ky',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='product',
            name='footer_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в нижней части сайта (Продукты)'),
        ),
        migrations.AddField(
            model_name='product',
            name='footer_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в нижней части сайта (Продукты)'),
        ),
        migrations.AddField(
            model_name='product',
            name='footer_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в нижней части сайта (Продукты)'),
        ),
        migrations.AddField(
            model_name='product',
            name='footer_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в нижней части сайта (Продукты)'),
        ),
        migrations.AddField(
            model_name='product',
            name='menu_title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в верхнем меню'),
        ),
        migrations.AddField(
            model_name='product',
            name='menu_title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в верхнем меню'),
        ),
        migrations.AddField(
            model_name='product',
            name='menu_title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в верхнем меню'),
        ),
        migrations.AddField(
            model_name='product',
            name='menu_title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в верхнем меню'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='product',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
    ]

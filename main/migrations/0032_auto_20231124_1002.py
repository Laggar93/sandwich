# Generated by Django 3.2.8 on 2023-11-24 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20231124_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='seo',
            name='description_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='seo',
            name='description_ky',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='seo',
            name='description_kz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='seo',
            name='description_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='seo',
            name='keywords_en',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='seo',
            name='keywords_ky',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='seo',
            name='keywords_kz',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='seo',
            name='keywords_ru',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Ключевые слова'),
        ),
        migrations.AddField(
            model_name='seo',
            name='title_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='seo',
            name='title_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='seo',
            name='title_kz',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AddField(
            model_name='seo',
            name='title_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
    ]
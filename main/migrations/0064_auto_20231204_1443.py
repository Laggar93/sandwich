# Generated by Django 3.2.8 on 2023-12-04 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_form_translation'),
    ]

    operations = [
        migrations.AddField(
            model_name='form_translation',
            name='department_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Укажите отдел'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='department_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Укажите отдел'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='department_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Укажите отдел'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='department_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Укажите отдел'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='name_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='name_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='name_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='name_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='ФИО'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='phone_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='phone_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='phone_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='phone_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Номер телефона'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='year_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Год рождения'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='year_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Год рождения'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='year_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Год рождения'),
        ),
        migrations.AddField(
            model_name='form_translation',
            name='year_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Год рождения'),
        ),
    ]

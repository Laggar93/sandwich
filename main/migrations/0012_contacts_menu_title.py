# Generated by Django 3.2.8 on 2023-11-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_vacancy_menu_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='menu_title',
            field=models.CharField(default=1, max_length=1000, verbose_name='Наименование в меню'),
            preserve_default=False,
        ),
    ]
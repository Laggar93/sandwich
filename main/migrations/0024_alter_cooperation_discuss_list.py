# Generated by Django 3.2.8 on 2023-11-23 16:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_alter_cooperation_discuss_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cooperation',
            name='discuss_list',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='Список из "Обсудим с вами"'),
        ),
    ]
# Generated by Django 3.2.8 on 2023-11-25 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_model_form_department'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_form',
            name='department',
        ),
    ]

# Generated by Django 3.2.8 on 2023-11-25 17:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_auto_20231125_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_form',
            old_name='form_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='model_form',
            old_name='form_phone',
            new_name='phone',
        ),
    ]

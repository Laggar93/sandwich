# Generated by Django 3.2.8 on 2023-11-23 16:27

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_about_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='compound_items',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
    ]

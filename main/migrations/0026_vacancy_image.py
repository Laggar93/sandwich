# Generated by Django 3.2.8 on 2023-11-24 07:44

from django.db import migrations, models
import sandwich.functions


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20231123_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='image',
            field=models.ImageField(default=1, upload_to=sandwich.functions.get_file_path, verbose_name='Первое изображение'),
            preserve_default=False,
        ),
    ]

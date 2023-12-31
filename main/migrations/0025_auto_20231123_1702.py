# Generated by Django 3.2.8 on 2023-11-23 17:02

from django.db import migrations, models
import sandwich.functions


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_cooperation_discuss_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='cooperation',
            name='second_image',
            field=models.ImageField(default=1, upload_to=sandwich.functions.get_file_path, verbose_name='Второе изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cooperation',
            name='image',
            field=models.ImageField(upload_to=sandwich.functions.get_file_path, verbose_name='Первое изображение'),
        ),
    ]

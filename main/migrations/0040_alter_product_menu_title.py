# Generated by Django 3.2.8 on 2023-11-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_auto_20231124_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='menu_title',
            field=models.CharField(max_length=1000, verbose_name='Наименование в верхнем меню'),
        ),
    ]
# Generated by Django 3.2.8 on 2023-11-23 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_intro_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='text',
            field=models.TextField(blank=True, verbose_name='Текст'),
        ),
    ]
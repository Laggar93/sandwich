# Generated by Django 3.2.8 on 2023-11-25 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_auto_20231125_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_form',
            name='year',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
    ]
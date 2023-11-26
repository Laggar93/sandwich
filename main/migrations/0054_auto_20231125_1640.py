# Generated by Django 3.2.8 on 2023-11-25 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0053_model_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_form',
            name='department',
            field=models.CharField(choices=[('1', 'Первый отдел'), ('2', 'Второй отдел'), ('3', 'Третий отдел')], default='1', max_length=1000, verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='model_form',
            name='year',
            field=models.DateField(null=True, verbose_name='Дата'),
        ),
    ]

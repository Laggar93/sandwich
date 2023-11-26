# Generated by Django 3.2.8 on 2023-11-25 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_remove_model_form_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='model_form',
            name='department',
            field=models.CharField(choices=[('1', 'Первый отдел'), ('2', 'Второй отдел'), ('3', 'Третий отдел')], default='1', max_length=1000, verbose_name='Отдел'),
        ),
    ]

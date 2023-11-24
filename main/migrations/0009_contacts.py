# Generated by Django 3.2.8 on 2023-11-22 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_phone', models.CharField(max_length=1000, verbose_name='Телефон для связи')),
                ('second_phone', models.CharField(max_length=1000, verbose_name='Телефон для оптовых клиентов')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Контакты',
                'verbose_name_plural': 'Контакты',
            },
        ),
    ]

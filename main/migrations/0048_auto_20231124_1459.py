# Generated by Django 3.2.8 on 2023-11-24 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0047_alter_vacancy_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='general',
            name='brandbook_button_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Брендбук"'),
        ),
        migrations.AddField(
            model_name='general',
            name='brandbook_button_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Брендбук"'),
        ),
        migrations.AddField(
            model_name='general',
            name='brandbook_button_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Брендбук"'),
        ),
        migrations.AddField(
            model_name='general',
            name='brandbook_button_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Брендбук"'),
        ),
        migrations.AddField(
            model_name='general',
            name='footer_title_cert_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню нижней части сайта "Сертификаты"'),
        ),
        migrations.AddField(
            model_name='general',
            name='footer_title_cert_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню нижней части сайта "Сертификаты"'),
        ),
        migrations.AddField(
            model_name='general',
            name='footer_title_cert_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню нижней части сайта "Сертификаты"'),
        ),
        migrations.AddField(
            model_name='general',
            name='footer_title_cert_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование в меню нижней части сайта "Сертификаты"'),
        ),
        migrations.AddField(
            model_name='general',
            name='org_name_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование организации (ОсОО)'),
        ),
        migrations.AddField(
            model_name='general',
            name='org_name_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование организации (ОсОО)'),
        ),
        migrations.AddField(
            model_name='general',
            name='org_name_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование организации (ОсОО)'),
        ),
        migrations.AddField(
            model_name='general',
            name='org_name_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Наименование организации (ОсОО)'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_confidence_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Соглашение о конфиденциальности"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_confidence_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Соглашение о конфиденциальности"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_confidence_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Соглашение о конфиденциальности"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_confidence_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Соглашение о конфиденциальности"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_media_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Для медийного сотрудничества"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_media_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Для медийного сотрудничества"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_media_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Для медийного сотрудничества"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_media_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Для медийного сотрудничества"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_work_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Мы работаем"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_work_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Мы работаем"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_work_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Мы работаем"'),
        ),
        migrations.AddField(
            model_name='general',
            name='title_work_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок "Мы работаем"'),
        ),
        migrations.AddField(
            model_name='general',
            name='up_button_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Наверх"'),
        ),
        migrations.AddField(
            model_name='general',
            name='up_button_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Наверх"'),
        ),
        migrations.AddField(
            model_name='general',
            name='up_button_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Наверх"'),
        ),
        migrations.AddField(
            model_name='general',
            name='up_button_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Кнопка "Наверх"'),
        ),
        migrations.AddField(
            model_name='general',
            name='work_days_en',
            field=models.CharField(max_length=1000, null=True, verbose_name='Дни работы'),
        ),
        migrations.AddField(
            model_name='general',
            name='work_days_kk',
            field=models.CharField(max_length=1000, null=True, verbose_name='Дни работы'),
        ),
        migrations.AddField(
            model_name='general',
            name='work_days_ky',
            field=models.CharField(max_length=1000, null=True, verbose_name='Дни работы'),
        ),
        migrations.AddField(
            model_name='general',
            name='work_days_ru',
            field=models.CharField(max_length=1000, null=True, verbose_name='Дни работы'),
        ),
    ]

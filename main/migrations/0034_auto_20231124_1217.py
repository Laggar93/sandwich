# Generated by Django 3.2.8 on 2023-11-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_auto_20231124_1149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='intro',
            old_name='buy_button_kz',
            new_name='buy_button_kk',
        ),
        migrations.RenameField(
            model_name='intro',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='intro',
            old_name='subtitle_kz',
            new_name='subtitle_kk',
        ),
        migrations.RenameField(
            model_name='intro',
            old_name='title_kz',
            new_name='title_kk',
        ),
        migrations.RenameField(
            model_name='seo',
            old_name='description_kz',
            new_name='description_kk',
        ),
        migrations.RenameField(
            model_name='seo',
            old_name='keywords_kz',
            new_name='keywords_kk',
        ),
        migrations.RenameField(
            model_name='seo',
            old_name='title_kz',
            new_name='title_kk',
        ),
    ]
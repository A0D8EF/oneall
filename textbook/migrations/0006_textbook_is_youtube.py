# Generated by Django 4.1.2 on 2022-10-27 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0005_rename_category_textbook_minor_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='is_youtube',
            field=models.BooleanField(default=False, verbose_name='Youtubeか'),
        ),
    ]
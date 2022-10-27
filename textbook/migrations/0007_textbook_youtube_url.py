# Generated by Django 4.1.2 on 2022-10-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0006_textbook_is_youtube'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='youtube_url',
            field=models.URLField(blank=True, null=True, verbose_name='YoutubeURL'),
        ),
    ]

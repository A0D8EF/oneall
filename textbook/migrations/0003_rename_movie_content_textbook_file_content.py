# Generated by Django 4.1.2 on 2022-10-25 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0002_remove_textbook_content_textbook_movie_content_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='textbook',
            old_name='movie_content',
            new_name='file_content',
        ),
    ]
# Generated by Django 4.1.2 on 2022-12-24 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0004_textbook_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='top_order',
            field=models.IntegerField(blank=True, null=True, verbose_name='トップ表示の順番'),
        ),
    ]
# Generated by Django 4.1.2 on 2022-12-24 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textbook', '0002_alter_minorcategory_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='textbook',
            name='is_top',
            field=models.BooleanField(default=False, verbose_name='トップ表示'),
        ),
    ]

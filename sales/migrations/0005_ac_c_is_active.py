# Generated by Django 4.1.2 on 2022-12-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_remove_ac_c_active_remove_question_ac_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='ac',
            name='c_is_active',
            field=models.BooleanField(default=True, verbose_name='Cさんの状態'),
        ),
    ]

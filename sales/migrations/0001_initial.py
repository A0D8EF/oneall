# Generated by Django 4.1.2 on 2022-10-29 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ABC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('abc_date', models.DateTimeField(verbose_name='ABC日時')),
            ],
        ),
        migrations.CreateModel(
            name='AC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('ac_date', models.DateTimeField(verbose_name='AC日時')),
                ('c_name', models.CharField(blank=True, max_length=10, null=True, verbose_name='Cさんの名前')),
                ('place', models.CharField(blank=True, max_length=200, null=True, verbose_name='AC場所')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('q_date', models.DateField(verbose_name='質問日')),
                ('ac', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.ac', verbose_name='対応するAC')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('interview_date', models.DateTimeField(verbose_name='面談日時')),
                ('abc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.abc', verbose_name='対応するABC')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='投稿日時')),
                ('contract_date', models.DateField(verbose_name='契約日時')),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.interview', verbose_name='対応する面談')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者')),
            ],
        ),
        migrations.AddField(
            model_name='abc',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.question', verbose_name='対応する質問'),
        ),
        migrations.AddField(
            model_name='abc',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='投稿者'),
        ),
    ]

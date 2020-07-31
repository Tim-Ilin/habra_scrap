# Generated by Django 3.0.8 on 2020-07-29 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('url', models.URLField(unique=True, verbose_name='Ссылка на статью')),
                ('body_text', models.TextField(verbose_name='Текст статьи')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления добавления')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='ParserError',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.CharField(max_length=200, verbose_name='Ошибка')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления добавления')),
            ],
            options={
                'verbose_name': 'Ошибка',
                'verbose_name_plural': 'Ошибки',
            },
        ),
    ]
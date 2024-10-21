# Generated by Django 4.2 on 2023-05-01 12:13

import Main.utils
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Жанр')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
            },
        ),
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Название списка')),
            ],
            options={
                'verbose_name': 'Список',
                'verbose_name_plural': 'Списки',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(upload_to=Main.utils.handle_manga_file, verbose_name='Обложка')),
                ('date_release', models.DateField(auto_now_add=True, verbose_name='Дата выхода')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('mark', models.FloatField(default=0.0, verbose_name='Оценка')),
                ('mark_count', models.IntegerField(default=0, verbose_name='Количество оценок')),
                ('author', models.CharField(max_length=64, verbose_name='Автор')),
                ('artist', models.CharField(max_length=64, verbose_name='Художник')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Status', to='Main.status', verbose_name='Статус тайтла')),
                ('status_translate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Status_translate', to='Main.status', verbose_name='Статус перевода')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.type', verbose_name='Тип')),
            ],
            options={
                'verbose_name': 'Манга',
                'verbose_name_plural': 'Манга',
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер главы')),
                ('name', models.CharField(blank=True, max_length=64, verbose_name='Название главы')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='Дата добавления')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.manga', verbose_name='Манга')),
            ],
            options={
                'verbose_name': 'Глава',
                'verbose_name_plural': 'Главы',
                'unique_together': {('manga', 'number')},
            },
        ),
        migrations.CreateModel(
            name='UserToManga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_add', models.DateField(auto_now_add=True, verbose_name='дата добавления в закладки')),
                ('list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Main.list', verbose_name='Список')),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.manga', verbose_name='Манга')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'В закладках у пользователя',
                'verbose_name_plural': 'В закладках у пользователей',
                'unique_together': {('user', 'manga')},
            },
        ),
        migrations.CreateModel(
            name='ChapterToPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=Main.utils.handle_chapter_file, verbose_name='Страница манги')),
                ('number', models.IntegerField(verbose_name='Номер страницы')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Main.chapter', verbose_name='Глава')),
            ],
            options={
                'verbose_name': 'Страница главы',
                'verbose_name_plural': 'Страницы глав',
                'unique_together': {('chapter', 'number', 'photo')},
            },
        ),
    ]

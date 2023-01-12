# Generated by Django 4.1.5 on 2023-01-12 08:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("notes_Vlad", "0009_notemodel_time_add"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(
                max_length=100, verbose_name="Наименование категории"
            ),
        ),
        migrations.AlterField(
            model_name="notemodel",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="notes_Vlad.category",
                verbose_name="Категория",
            ),
        ),
        migrations.AlterField(
            model_name="notemodel",
            name="content",
            field=models.CharField(max_length=100, verbose_name="Заметка"),
        ),
        migrations.AlterField(
            model_name="notemodel",
            name="reminder",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Напоминание"
            ),
        ),
        migrations.AlterField(
            model_name="notemodel",
            name="text",
            field=models.TextField(blank=True, null=True, verbose_name="Текст заметки"),
        ),
        migrations.AlterField(
            model_name="notemodel",
            name="time_add",
            field=models.DateTimeField(
                default=datetime.datetime.now, verbose_name="Время добавления заметки"
            ),
        ),
    ]

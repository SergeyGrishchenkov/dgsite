# Generated by Django 4.1.5 on 2023-01-12 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes_Vlad", "0013_alter_notemodel_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notemodel",
            name="content",
            field=models.CharField(max_length=50, verbose_name="Заметка"),
        ),
    ]
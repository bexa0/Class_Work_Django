# Generated by Django 4.2.6 on 2023-10-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_reader_liked_books'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(max_length=255, null=True, unique=True),
        ),
    ]
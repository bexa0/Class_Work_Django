# Generated by Django 4.2.6 on 2023-10-23 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_testtable'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testtable',
            name='id',
        ),
        migrations.AlterField(
            model_name='testtable',
            name='second_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
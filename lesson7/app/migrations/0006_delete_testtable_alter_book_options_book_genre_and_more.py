# Generated by Django 4.2.6 on 2023-10-23 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_testtable_id_alter_testtable_second_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestTable',
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Книга'},
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.PositiveIntegerField(choices=[(1, 'Фентези'), (2, 'Фантастика'), (3, 'Детектив')], null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='age',
            field=models.PositiveIntegerField(default=60, help_text='Возраст автора', unique=True),
        ),
    ]

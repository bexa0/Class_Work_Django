from django.db import models

# Create your models here.


# class TestTable(models.Model):
#     second_id = models.IntegerField(primary_key=True)
#
#     def __str__(self):
#         return f'{self.second_id}'


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    age = models.PositiveIntegerField(default=60, unique=True, help_text='Возраст автора')

    class Meta:
        app_label = 'app'
        ordering = ['first_name', 'age']
        unique_together = ('first_name', 'last_name', 'age')
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.age}'


GENRE_CHOICE = (
    (1, 'Фентези'),
    (2, 'Фантастика'),
    (3, 'Детектив')
)


class Book(models.Model):
    title = models.CharField(max_length=255)
    genre = models.PositiveIntegerField(null=True, choices=GENRE_CHOICE)
    pages = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Книга'

    def __str__(self):
        return f'{self.title} - {self.pages}'
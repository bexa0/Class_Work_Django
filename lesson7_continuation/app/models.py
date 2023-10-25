from django.db import models

# Create your models here.
from django.utils.text import slugify


class Ticket(models.Model):
    ticket_id = models.PositiveIntegerField(default=1111)

    def __str__(self):
        return f'{self.pk} - {self.ticket_id}'


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
        # unique_together = ('first_name', 'last_name', 'age')
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

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(max_length=255, null=True, unique=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        # нельзя поменять slug потому что есть проверка if not
        if not self.slug:
            self.slug = slugify(f'{self.title}-{self.pages}-{self.author.first_name}')

        # тут можно поменять slug
        # self.slug = slugify(f'{self.title}-{self.pages}-{self.author.first_name}')

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name = 'Книга'

    def __str__(self):
        return f'{self.title} - {self.pages}'

    # def get_absolute_url(self):
    #     return f'book/{self.pk}'

    def get_absolute_url(self):
        return f'book/{self.slug}'


class Reader(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)

    liked_books = models.ManyToManyField(Book)

    def __str__(self):
        return f'{self.first_name} - {self.last_name}'
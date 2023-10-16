from django.db import models


class newBook(models.Model):
    title = models.CharField(max_length=50)

    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=255)

    author_name = models.CharField(max_length=50)
    author_surname = models.CharField(max_length=50)

    publication_year = models.PositiveIntegerField()
    page_count = models.PositiveIntegerField()

    genre = models.CharField(max_length=50)

    description = models.IntegerField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.author_surname}"


class Reader(models.Model):
    name = models.CharField(max_length=2)
    surname = models.CharField(max_length=2)
    age = models.PositiveIntegerField()
    address = models.PositiveIntegerField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.surname} - {self.age}"


class BookRent(models.Model):
    book_title = models.CharField(max_length=50)
    return_date = models.DateField()
    reader_surname = models.CharField(max_length=50)
    rent_date = models.DateField()

    def __str__(self):
        return f"{self.book_title} was rent to {self.reader_surname}: {self.rent_date} - {self.return_date}"


from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f'title - {self.title}, price - {self.price}'

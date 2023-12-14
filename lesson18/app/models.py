from django.db import models
from random import randint, choices
from string import ascii_letters
from django.template.defaultfilters import slugify


class Product(models.Model):
    name = models.CharField(max_length=255, blank=True)
    price = models.PositiveIntegerField(blank=True)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField(default=10, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.price}"

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):

        if not self.name:
            self.name = ''.join(choices(ascii_letters, k=20))
            self.price = randint(1000, 10000)
            self.description = ''.join(choices(ascii_letters, k=200))
        self.slug = slugify(f"{self.name} - {self.price}")

        return super().save(force_insert, force_update, using, update_fields)


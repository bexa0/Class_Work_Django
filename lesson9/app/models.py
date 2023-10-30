from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField(default=100)
    slug = models.SlugField(max_length=255, blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(f'{self.name} - {self.category} - {self.price}')
        super(Product, self).save(force_insert=False, force_update=False, using=None, update_fields=None)

    def __str__(self):
        return f'{self.name} - {self.price}'

    def get_absolute_url(self):
        # return f'{self.pk}'
        return reverse('p_detail', args=(self.pk,))

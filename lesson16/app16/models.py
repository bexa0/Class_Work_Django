from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_slug': self.slug})


    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(f'{self.title}')
        super().save(force_insert, force_update, using, update_fields)
        return f'{self.title}'

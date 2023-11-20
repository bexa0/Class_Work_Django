from django.db import models


class FeedBack(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    text = models.TextField()

    def __str__(self):
        return f'{self.name} - {self.text}'

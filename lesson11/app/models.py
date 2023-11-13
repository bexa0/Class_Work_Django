from django.db import models


class Human(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.first_name} - {self.last_name} - {self.age}'

from django.db import models


class Human(models.Model):
    name = models.CharField(max_length=255)
    age = models.CharField(max_length=255)
    favorite_music = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.age}'

    def get_absolute_url(self):
        return f'//{self.pk}'


# class RegHuman(models.Model):
#     name = models.CharField(max_length=255)
#     age = models.PositiveIntegerField()
#     music = models.CharField(max_length=255)
#     favorite_hobbies = models.CharField(max_length=255)
#
#     def __str__(self):
#         return f'{self.name} - {self.age} - {self.music} - {self.favorite_hobbies}'
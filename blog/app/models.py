from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.name} - {self.age}'


class FeedBackPost(models.Model):
    id = models.ForeignKey(Post, primary_key=True, on_delete=models.CASCADE)
    author_post = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    description_post = models.TextField()
    quantity_likes = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.author_post} - {self.title}'

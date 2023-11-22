from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    avg_time = models.PositiveIntegerField()


class Module(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    avg_time = models.PositiveIntegerField()


class Lesson(models.Model):
    name_lesson = models.CharField(max_length=255)
    quantity_lessons = models.PositiveIntegerField()



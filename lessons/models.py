from django.db import models


class Lesson(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True, null=True)

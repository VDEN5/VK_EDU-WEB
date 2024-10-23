from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    tags = models.CharField(max_length=100)
    likes = models.IntegerField(default=0)
    answer_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
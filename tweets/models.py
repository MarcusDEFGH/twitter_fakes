from django.db import models

from tags.models import Tag
from users.models import User


class Tweet(models.Model):
    text = models.CharField(max_length=280)
    date = models.DateTimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

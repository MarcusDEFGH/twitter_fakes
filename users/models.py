from django.db import models

from tags.models import Tag


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    tweets = models.PositiveIntegerField()
    following = models.PositiveIntegerField()
    followers = models.PositiveIntegerField()
    potential_fake = models.BooleanField(default=False)
    is_fake = models.BooleanField(default=False)
    reported = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    tag = models.ManyToManyField(Tag)

    @property
    def status(self):
        status_dict = {'potential_fake': 'That may be a fake account.',
                       'is_fake': 'That is a fake accout.',
                       'reported': 'That account was already reported.',
                       'banned': 'That account has already been banned.'}
        for key in status_dict.keys():
            if getattr(self, key):
                return status_dict[key]
        return 'That account has not been verified yet.'

    def __str__(self):
        return f'{self.username} - {self.status}'

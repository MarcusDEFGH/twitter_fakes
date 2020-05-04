from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=40)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} - active: {self.is_active}'

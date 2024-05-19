from django.db import models

# Create your models here.

from django.db import models

class Place(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.name)
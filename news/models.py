import calendar
import time

from django.db import models


# Create your models here.

class Headline(models.Model):
    gmt = time.gmtime()

    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    url = models.TextField()
    date = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

import time

from django.db import models


class Articles(models.Model):
    gmt = time.gmtime()

    title = models.CharField(max_length=255)
    image = models.URLField(null=True, blank=True)
    url = models.URLField(null=True)
    date = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

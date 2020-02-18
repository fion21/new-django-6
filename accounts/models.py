from django.db import models
from datetime import datetime
from django.core.files.images import ImageFile


class Addprop(models.Model):

    city = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.city

    def delete(self, *args, **kwargs):
        self.cover.delete()
        super().delete(*args, **kwargs)

import datetime
from django.db import models
from django.utils import timezone

class books(models.Model):
    book_id = models.IntegerField(blank=False)
    book_name = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    def __str__(self):              # __unicode__ on Python 2
        return self.book_name

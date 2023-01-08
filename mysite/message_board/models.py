from datetime import date, datetime
from django.db import models
from django.utils import timezone


class Entry(models.Model):
    name_A = models.CharField(max_length=50)
    name_B = models.CharField(max_length=50)
    pub_date = models.DateTimeField(blank=True, null=True)
    message = models.CharField(max_length=500)

    def __str__(self):
        return self.name_A + " " + self.pub_date


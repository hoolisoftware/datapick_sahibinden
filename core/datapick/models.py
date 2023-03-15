from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=55)
    price = models.CharField(max_length=55)
    location = models.CharField(max_length=55)
    date = models.CharField(max_length=55)

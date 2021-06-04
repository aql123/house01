from django.db import models

class Info(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    types = models.CharField(max_length=255)
    area = models.FloatField()
    floor = models.CharField(max_length=255)
    elevator = models.CharField(max_length=255)
    fuel = models.CharField(max_length=255)
    log = models.FloatField()
    lat = models.FloatField()
    city = models.CharField(max_length=255)
    class Meta:
        db_table = 'poll_info'

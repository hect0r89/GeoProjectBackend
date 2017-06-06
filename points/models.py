from django.db import models


# Create your models here.
class Point(models.Model):
    lat = models.FloatField('Latitud', blank=False, null=False)
    lon = models.FloatField('Longitud', blank=False, null=False)
    radius = models.IntegerField('Radio', blank=False, null=False, default=150)
    message = models.CharField('Mensaje', blank=False, null=False, max_length=200)
    device_id = models.CharField('Id dispositivo', blank=True, null=True, max_length=500)

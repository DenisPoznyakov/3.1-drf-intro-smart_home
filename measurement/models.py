from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name =models.CharField(max_length=100)
    description = models.CharField(max_length=100)

class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(decimal_places=1, max_digits=4)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
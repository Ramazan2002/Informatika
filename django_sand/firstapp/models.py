from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    height = models.FloatField()
    weight = models.FloatField()
    gender = models.CharField(max_length=1)
    size = models.CharField(max_length=3)
    obraschenie = models.CharField(max_length=3)
    imt = models.FloatField()
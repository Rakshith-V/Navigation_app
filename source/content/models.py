
from django.db import models


class Coordinate(models.Model):
    coordinate= models.CharField(max_length=100)
from django.db import models

class insert(models.Model):
    name = models.CharField(max_length=30)
    pw = models.CharField(max_length=12)

from django.db import models

# Create your models here.
class SearchModel(models.Model):
    search = models.CharField(max_length=100)

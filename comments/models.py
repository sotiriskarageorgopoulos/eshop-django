from django.db import models
from main_page.models import (validate_email)
# Create your models here.
class CommentsModel(models.Model):
    username = models.CharField(max_length=100)
    comment = models.TextField(max_length=800)
    email = models.EmailField(max_length=100,validators=[validate_email])
    date = models.DateTimeField(blank=True)
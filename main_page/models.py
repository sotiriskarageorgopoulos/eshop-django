from django.db import models
from django.core.exceptions import ValidationError
import re

def validate_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(email_regex,email):
        return email
    else:
        ValidationError("This is not an email!")

# Create your models here.
class SearchModel(models.Model):
    search = models.CharField(max_length=100)

class ContactUsModel(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(validators=[validate_email])
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=400)
from django.db import models
from django.core.exceptions import ValidationError
import re

# Create your models here.
def validate_email(email):
    email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(email_regex,email):
        return email
    else:
        ValidationError("This is not an email!")

def validate_tel(tel):
    tel_regex = r'^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$'
    if re.fullmatch(tel_regex,tel):
        return tel
    else:
        ValidationError("This is not a valid telephone number!")


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,validators=[validate_email])
    password = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    tel = models.CharField(max_length=10,validators=[validate_tel])
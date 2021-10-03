from django.db import models
from django.core.exceptions import ValidationError
import uuid
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

class OrderModel(models.Model):
    order_id = models.CharField(max_length=100,primary_key=True,editable=False)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,validators=[validate_email])
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    tel = models.CharField(max_length=10,validators=[validate_tel])
    payment_method = models.CharField(max_length=100)
    credit_card_number = models.CharField(max_length=16,null=True)
    ccv = models.CharField(max_length=3,null=True)
    total_cost = models.FloatField()

    def save(self,*args,**kwargs):
        if not self.order_id:
            self.order_id = str(uuid.uuid4())
        return super(OrderModel,self).save(*args,**kwargs)

class OrderedProductModel(models.Model):
    order_id = models.ForeignKey('OrderModel',on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    pieces = models.IntegerField(default=1)





from django.db import models
import uuid

clothes_category = (
    ("t-shirt","t-shirt"),
    ("pants","pants"),
    ("jeans","jeans"),
    ("jackets","jackets")
)

colors = (
    ("RED","RED"),
    ("WHITE","WHITE"),
    ("BLACK","BLACK"),
    ("ORANGE","ORANGE"),
    ("BROWN","BROWN"),
    ("YELLOW","YELLOW"),
    ("PURPLE","PURPLE"),
    ("PINK","PINK"),
    ("GREEN","GREEN"),
    ("BLUE","BLUE")
)

sizes = (
    ("XS","XS"),
    ("S","S"),
    ("L","L"),
    ("XL","XL"),
    ("XXL","XXL")
)

# Create your models here.
class ClothesModel(models.Model):
    code = models.CharField(max_length=100,editable=False,primary_key=True)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    description = models.TextField(max_length=400)
    category = models.CharField(choices=clothes_category,max_length=100)
    image = models.ImageField(upload_to='images/')

    #create dynamically primary keys
    def save(self,*args,**kwargs): 
        if not self.code:
            self.code = str(uuid.uuid4())
        return super(ClothesModel,self).save(*args,**kwargs)

class ShoesModel(models.Model):
    code = models.CharField(max_length=100,editable=False,primary_key=True)
    brand = models.CharField(max_length=100)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    description = models.TextField(max_length=400)
    image = models.ImageField(upload_to='images/')

    #create dynamically primary keys
    def save(self,*args,**kwargs):
        if not self.code:
            self.code = str(uuid.uuid4())
        return super(ShoesModel,self).save(*args,**kwargs)

class ClothesDetailsModel(models.Model):
    code = models.ForeignKey('ClothesModel',on_delete=models.CASCADE)
    color = models.CharField(max_length=100,choices=colors)  
    size = models.CharField(max_length=100,choices=sizes) 
    availability = models.BooleanField()

class ShoesDetailsModel(models.Model):
    code = models.ForeignKey('ShoesModel',on_delete=models.CASCADE)
    color = models.CharField(max_length=100,choices=colors)  
    size_number = models.IntegerField() 
    availability = models.BooleanField()
    

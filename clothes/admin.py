from django.contrib import admin
from clothes.models import (ClothesModel, ShoesModel,ClothesDetailsModel,ShoesDetailsModel)
# Register your models here.
admin.site.register(ClothesModel)
admin.site.register(ShoesModel)
admin.site.register(ClothesDetailsModel)
admin.site.register(ShoesDetailsModel)
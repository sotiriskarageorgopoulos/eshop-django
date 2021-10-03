from django.contrib import admin
from order.models import (OrderModel,OrderedProductModel)
# Register your models here.
admin.site.register(OrderModel)
admin.site.register(OrderedProductModel)
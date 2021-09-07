from django.urls import path
from clothes.views import (t_shirts_view,
pants_view,jackets_view,jeans_view,shoes_view,
t_shirt_view,pant_view,jacket_view,jean_view,shoe_view)

urlpatterns = [
    path('t_shirts/',t_shirts_view,name="t_shirts"),
    path('pants/',pants_view,name="pants"),
    path('jackets/',jackets_view,name="jackets"),
    path('jeans/',jeans_view,name="jeans"),
    path('shoes/',shoes_view,name="shoes"),
    path('t_shirt/<slug:code>',t_shirt_view,name="t_shirt"),
    path('pant/<slug:code>',pant_view,name="pant"),
    path('jacket/<slug:code>',jacket_view,name="jacket"),
    path('jean/<slug:code>',jean_view,name="jean"),
    path('shoe/<slug:code>',shoe_view,name="shoe")
]
from django.urls import path
from register.views import (register_view)

urlpatterns =  [
    path('',register_view,name='register')
]
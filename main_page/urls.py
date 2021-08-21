from django.urls import path 
from main_page.views import (main_page_view)

urlpatterns = [
    path('',main_page_view,name='main_page')
]

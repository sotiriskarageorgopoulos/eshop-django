from django.urls import path 
from main_page.views import (main_page_view,searched_item_view)

urlpatterns = [
    path('',main_page_view,name='main_page'),
    path('searched_items',main_page_view,name='searched_items'),
    path('search_item/<slug:code>',searched_item_view,name='searched_item')
]

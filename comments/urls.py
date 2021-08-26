from django.urls import path
from comments.views import (comments_view)

urlpatterns = [
    path('',comments_view,name='comments')
]
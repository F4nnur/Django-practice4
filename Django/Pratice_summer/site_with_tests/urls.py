from django.urls import path
from .views import *

urlpatterns = [
    path('', inndex, name='home')
]

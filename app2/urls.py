from django.urls import path
from app2.views import *

app_name='sonu'

urlpatterns = [
    path('pashupati/',pashupati,name='pashupati'),
]

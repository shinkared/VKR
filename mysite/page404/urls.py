from django.urls import path
from .views import *

urlpatterns = [

    path('<str:text_content>/', text, name='text'),
]

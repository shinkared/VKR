from django.urls import path
from .views import *

urlpatterns = [

    path('<path:text_content>/', text, name='text'),
]

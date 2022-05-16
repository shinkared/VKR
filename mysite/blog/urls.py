from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='bloghome'),
    path('category/<str:slug>/', get_category, name='category')
]
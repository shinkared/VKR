from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

def text(request, text_content):
    text_content = text_content+ 'dun4ik'
    return render(request, 'base - Copy.html', {"content": text_content, "text2": 'tttttttttttt',})
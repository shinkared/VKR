from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

def text(request, text_content):

    return render(request, 'base.html', {"content": text_content})
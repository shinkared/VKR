from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

def text(request, text_content):

    return render(request, 'news/view_news.html', {"news_item": text_content})
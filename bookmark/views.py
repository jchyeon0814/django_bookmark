from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import WebSite

class ListView(generic.ListView):
    template_name = 'bookmark/list.html'
    context_object_name = 'webSite_list'
    
    def get_queryset(self):
        return WebSite.objects.order_by('id')[:6]
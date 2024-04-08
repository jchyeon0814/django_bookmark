from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views import generic
from django.http import HttpResponseRedirect

from .models import WebSite


class BookmarkListView(ListView):
    model = WebSite
    template_name = "bookmark/list.html"
    paginate_by = 6
    
class AddView(generic.TemplateView):
    template_name = "bookmark/add.html"


class ModifyView(generic.DetailView):
    model = WebSite
    template_name = "bookmark/modify.html"


def add(request):
    webSite = WebSite()
    webSite.siteName = request.POST['siteName']
    webSite.url = request.POST['url']
    webSite.save();
    
    return HttpResponseRedirect("/bookmark")

class DeleteView:
    pass  # 임시

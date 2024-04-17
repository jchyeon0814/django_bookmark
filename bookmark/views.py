from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views import generic
from django.http import HttpResponseRedirect

from .models import WebSite

'''
북마크 리스트 페이지
django.views.generic.list.ListView 상속하여 구현
'''
class BookmarkListView(ListView):
    model = WebSite
    template_name = "bookmark/list.html"
    paginate_by = 6
    
class AddView(generic.TemplateView):
    template_name = "bookmark/add.html"

'''
북마크 추가 페이지
django.views.generic.edit.CreateView 상속하여 구현
'''
class BookmarkCreateView(CreateView):
    model = WebSite
    fields = ['siteName', 'url']
    template_name = "bookmark/add.html"
    success_url = reverse_lazy('bookmark:list') #model(WebSite)로 POST요청이 들어와서 정상 저장됐을 때 호출될 페이지
    
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

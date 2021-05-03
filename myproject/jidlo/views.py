from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import *


def index(request):
    return render(request, template_name='index.html')


class JidloListView(ListView):
    model = Jidlo
    context_object_name = 'jidlo_list'
    template_name = 'list.html'


class JidloDetailView(DetailView):
    model = Jidlo
    context_object_name = 'jidlo'
    template_name = 'detail.html'


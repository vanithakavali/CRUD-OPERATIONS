from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,DetailView,CreateView

class schoollist(ListView):
    model=School
    context_object_name='allso'

class SchoolDetail(DetailView):
    model=School
    context_object_name='DOSI'
    template_name='app/school_detail.html'

class SchoolCreate(CreateView):
    model=School
    fields="__all__"

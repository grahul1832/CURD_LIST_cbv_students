from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from app.models import *



class SchoolList(ListView):
    model=School
    context_object_name='ALLSO'
    template_name='app\school_list.html'
    




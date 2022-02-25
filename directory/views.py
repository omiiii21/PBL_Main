from django.shortcuts import render
from django.views.generic import ListView
from .models import Directory

def directory(request):
    return render(request, 'directory.html',{})

class DirectoryView(ListView):
    model = Directory
    template_name = 'directory.html'
    
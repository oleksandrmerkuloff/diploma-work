from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home_page(request):
    return render(request, 'home.html')

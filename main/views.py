from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("<h3>Hello World! This Is GCI</h3>")
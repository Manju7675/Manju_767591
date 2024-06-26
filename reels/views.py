from django.shortcuts import render
from django.http import HttpResponse


def reel(request):
    return HttpResponse("This is a reel")

# Create your views here.

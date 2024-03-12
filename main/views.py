from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("hello Nikhil")
# Create your views here.


def new(request):
    return HttpResponse("you opened new")
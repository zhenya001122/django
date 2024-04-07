from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return HttpResponse("Начало...")


def categories(request):
    return HttpResponse("Здесь юудут категории")

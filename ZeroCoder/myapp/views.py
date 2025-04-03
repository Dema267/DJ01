from django.shortcuts import render
from django.http import HttpResponse

def data_page(request):
    return HttpResponse("Это страница DATA. Привет, Django!")

def test_page(request):
    return HttpResponse("Это страница TEST. Работает!")



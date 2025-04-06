from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):  # Новый view для главной страницы
    return HttpResponse("Главная страница. Перейдите на /data/ или /test/")

def data_page(request):
    return HttpResponse("Это страница DATA. Привет, Django!")

def test_page(request):
    return HttpResponse("Это страница TEST. Работает!")
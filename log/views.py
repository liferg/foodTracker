from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .code import searchFood

def logView(request):
    return render(request, 'log.html')

def addFoodView(request):
    return render(request, 'addFoodPage.html')

def foodSelectedView(request):
    return render(request, 'foodSelectedPage.html')

def searchEnteredFood(request):
    result = searchFood()
    return render(result, 'addFoodPage.html')

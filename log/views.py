from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

def logView(request):
    return render(request, 'log.html')

def addFoodView(request):
    return render(request, 'addFoodPage.html')

def foodSelectedView(request):
    return render(request, 'foodSelectedPage.html')
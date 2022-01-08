from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
import http.client

def logView(request):
    return render(request, 'log.html')

def addFoodView(request):
    return render(request, 'addFoodPage.html')

def foodSelectedView(request):
    return render(request, 'foodSelectedPage.html')

def searchEnteredFood(request):
    print(data.decode("utf-8"))
    search = request.GET.get('searchTerm')
    response = {
       'search' : search
    }
    return JsonResponse(response)

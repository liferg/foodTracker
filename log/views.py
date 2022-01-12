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

def searchResults(request):
    if request.method == "POST":
        searchTerm = request.POST['searchTerm']
        foods = searchFood(searchTerm)
        return render(request, 'addFoodPageSearchResults.html', {'searchTerm': searchTerm, 'foods':foods})
    else:
        return render(request, 'addFoodPageSearchResults.html')

def selectFood(request):
    if request.method == "POST":
        selectedFood = request.POST['selectedFood']
        return render(request, 'foodSelectedPage.html', {'selectedFood': selectedFood})
    else:
        return render(request, 'foodSelectedPage.html')

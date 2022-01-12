from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .code import searchFood
from .models import Food, SingleDayFood, User

def logView(request):
    return render(request, 'log.html')

def addFoodView(request):
    Food.objects.all().delete()
    return render(request, 'addFoodPage.html')

def foodSelectedView(request):
    return render(request, 'foodSelectedPage.html')

def searchResults(request):
    if request.method == "POST":
        searchTerm = request.POST['searchTerm']
        searchFood(searchTerm)
        foods = Food.objects.all()
        return render(request, 'addFoodPageSearchResults.html', {'searchTerm': searchTerm, 'foods': foods})
    else:
        return render(request, 'addFoodPageSearchResults.html')

def selectFood(request, foodId):
    selectedFood = Food.objects.get(pk=foodId)
    foods = Food.objects.all()
    print(selectedFood.description)
    return render(request, 'foodSelectedPage.html', {'foods': foods, 'selectedFood': selectedFood})

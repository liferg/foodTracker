import requests
from .models import *

apiKey = 'oSCPMwfMvZkiRn3AwPrcf17WF5wVVqm0eUAxf3Ha'
descriptions = []

def searchFood(searchTerm):
    headers = {
        'query': searchTerm,
        'pageSize': '8',
        'api_key': apiKey
    }
    url = "https://api.nal.usda.gov/fdc/v1/foods/search?"
    response = requests.get(url, headers)
    data = response.json()
    for result in data.get('foods'):
        description = result.get('description')
        brandName = ''
        if (result.get('brandName')):
            brandName = result.get('brandName')
        else:
            brandName = ''
        servingSize = result.get('servingSize')
        servingSizeUnit = result.get('servingSizeUnit')
        food = Food(description=description, brand=brandName, servingSize=servingSize, servingSizeUnit=servingSizeUnit)
        for nutrient in result.get('foodNutrients'):
            if (nutrient.get('nutrientName') == 'Energy'):
                calories = nutrient.get('value')
                food.calories = calories;
            if (nutrient.get('nutrientName') == 'Protein'):
                gramsProtein = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsProtein *= 1000
                food.gramsProtein = gramsProtein
            if (nutrient.get('nutrientName') =='Carbohydrate, by difference'):
                gramsCarb = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsCarb *= 1000
                food.gramsCarb = gramsCarb
            if (nutrient.get('nutrientName') == 'Total lipid (fat)'):
                gramsFat = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsFat *= 1000
                food.gramsFat = gramsFat
            if (nutrient.get('nutrientName') == 'Fiber, total dietary'):
                gramsFiber = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsFiber *= 1000 
                food.gramsFiber = gramsFiber
        food.save()



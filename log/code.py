import requests

def searchFood():
    
    url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=8&api_key=oSCPMwfMvZkiRn3AwPrcf17WF5wVVqm0eUAxf3Ha"
    response = requests.get(url)
    data = response.json()
    for result in data.get('foods'):
        description = result.get('description')
        brandName = result.get('brandName')
        servingSizeUnit = result.get('servingSizeUnit')
        servingSize = result.get('servingSize')
        for nutrient in result.get('foodNutrients'):
            if (nutrient.get('nutrientName') == 'Energy'):
                calories = nutrient.get('value')
            if (nutrient.get('nutrientName') == 'Protein'):
                gramsProtein = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsProtein *= 1000
            if (nutrient.get('nutrientName') =='Carbohydrate, by difference'):
                gramsCarb = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsCarb *= 1000
            if (nutrient.get('nutrientName') == 'Total lipid (fat)'):
                gramsFat = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsFat *= 1000
            if (nutrient.get('nutrientName') == 'Fiber, total dietary'):
                gramsFiber = nutrient.get('value')
                if (nutrient.get('unitName') == 'mg'):
                    gramsFiber *= 1000
    print("hello! searchFood() function worked!")

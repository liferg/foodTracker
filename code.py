import requests

url = "https://api.nal.usda.gov/fdc/v1/foods/search?query=apple&pageSize=1&api_key=oSCPMwfMvZkiRn3AwPrcf17WF5wVVqm0eUAxf3Ha"
response = requests.get(url)
data = response.json()
print(data.get('foods')[0].get('foodNutrients'))

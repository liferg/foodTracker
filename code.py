import http.client

def searchFood(foodName):   
    conn = http.client.HTTPSConnection("api.nal.usda.gov")
    payload = ''
    headers = {}
    conn.request("GET", "/fdc/v1/foods/search?query=apple&pageSize=1&api_key=oSCPMwfMvZkiRn3AwPrcf17WF5wVVqm0eUAxf3Ha", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
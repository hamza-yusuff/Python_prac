import requests
responses=requests.get("https://api.spoonacular.com/recipes/findByIngredients",params={'apiKey':"f8cae3dbcd1a4373bd2aba5b1fae1cfc",'ingredients':["apples","flour","sugar"],"number":"2"},)
for response in responses.json():
    print(response)

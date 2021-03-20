from clarifai.rest import ClarifaiApp
import requests
app=ClarifaiApp(api_key="641b399837864b6fbda468ae7cb4ff30")
model = app.models.get(model_id="bd367be194cf45149e75f01d59f77ba7")
query=[]
responses = model.predict_by_filename(filename='food.jpg')
for response in responses['outputs'][0]['data']['concepts']:
    if response['value'] > 0.2:
        query.append(response['name'])


#recipe finder
recipes=requests.get("https://api.spoonacular.com/recipes/findByIngredients",params={'apiKey':"f8cae3dbcd1a4373bd2aba5b1fae1cfc",'ingredients':query,"number":"2"},)
for recipe in recipes.json():
    print(recipe['title'])

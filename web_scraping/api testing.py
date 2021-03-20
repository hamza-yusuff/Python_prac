from __future__ import print_function
import time
import cloudmersive_image_api_client
from cloudmersive_image_api_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: Apikey
configuration = cloudmersive_image_api_client.Configuration()
configuration.api_key['Apikey'] = '10605bd6-cbad-444f-9641-6ffb15fc0a89'



# create an instance of the API class
api_instance = cloudmersive_image_api_client.RecognizeApi(cloudmersive_image_api_client.ApiClient(configuration))
image_file = 'F:\Hamza Y\web_scraping\fridge1.jpg' # file | Image file to perform the operation on.  Common file formats such as PNG, JPEG are supported.

try:
    # Detect objects including types and locations in an image
    api_response = api_instance.recognize_detect_objects(image_file)
    print(api_response)
except ApiException as e:
    print("Exception when calling RecognizeApi->recognize_detect_objects: %s\n" % e)

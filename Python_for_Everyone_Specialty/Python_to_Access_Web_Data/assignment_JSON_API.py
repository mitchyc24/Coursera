'''
Welcome Mitchell Carroll from Using Python to Access Web Data

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like. If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint is as shown above. You will get different results from the geojson and json endpoints so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJy0Uc1Zmym4gR3fmAYmWNuac".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 2433 characters
Place id ChIJy0Uc1Zmym4gR3fmAYmWNuac
'''

import json
import urllib.request, urllib.parse, urllib.error
import ssl

api_key = 42
url = "http://py4e-data.dr-chuck.net/json?" 
        
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    location = input("Input location:")
    if len(location) < 1: break

    parms = dict()
    parms["address"] = location
    parms["key"] = api_key
    url += urllib.parse.urlencode(parms)
    print("Retrieving: ", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "bytes of data")

    try:
        js = json.loads(data)
    except: 
        js = None
        print("URL Parsing Error")

    if not js or "status" not in js or js["status"] != "OK":
        print("==========FAILURE TO RETRIEVE DATA==============")
        print(data)
        continue

    print("Place Id:", js["results"][0]["place_id"])
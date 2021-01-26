import urllib.request, urllib.parse, urllib.error
import json

serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

while True:
    address = input("Enter Address/Location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({"address": address}) + "&key=AIzaSyC_BCZant9pldLIVDx93xs-7jCFyn6L5Ao"

    print("Retrieving", url)
    handle = urllib.request.urlopen(url)
    data = handle.read().decode()
    print("Retrieved", len(data), "characters of data")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("===== FAILURE TO RETRIEVE =====")
        print(data)
        continue

    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print("lat:", lat, "long:", lng)

    location = js["results"][0]["formatted_address"]
    print("location:", location)
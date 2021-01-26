'''
2020-08-04 Mitchell Carroll 
Attempting to write a short program that will take an XML file and parse values into objects
that can be callable later.

This is the foundation to what I hope to program at 414 Sqn for our Emitter Database and extract from CDNMDLT generated XMLs into 
a python/sql database.
'''

#Tasks:
#Get URL
url = "https://www.w3schools.com/xml/plant_catalog.xml"

#Fetch XML file
import urllib.request
xml_handle = urllib.request.urlopen(url)
xml_str = xml_handle.read().decode()

#Read XML file
import xml.etree.ElementTree as ET
xml_read = ET.fromstring(xml_str)

#define object structure
from plant import Plant

list_of_plants = []

def create_plants(xml_read):
    for plant in xml_read:
        #create kwargs for each plant
        plant_dict = {}
        for attribute in list(plant):
            plant_dict[attribute.tag] = attribute.text
        
        list_of_plants.append(Plant(**plant_dict))
    return list_of_plants

        #add plant to list
        #list_of_plants.append(Plant(kwargs))

list_of_plants = create_plants(xml_read)

for plant in list_of_plants:
    for attribute, value in plant.__dict__.items():
        pass
        #print(attribute, value)

   

def get_average_price(list_of_plants):
    total = 0
    for plant in list_of_plants:
        total += plant.get_price()
    return round(total/len(list_of_plants),2)

print(f"The average price of plants is ${get_average_price(list_of_plants)}")

    

#Commit to object oriented data structure. 

#Display and navigate information.
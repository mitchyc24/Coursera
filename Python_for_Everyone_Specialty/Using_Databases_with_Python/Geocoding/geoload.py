import urllib
from urllib import parse
from urllib import request
import sqlite3
import json
import time
import ssl

from inspect import getsourcefile
from os.path import abspath
from os import path
import os


def get_path(func):
    return(abspath(getsourcefile(func)))


def get_dir(func):
    return(path.dirname(abspath(getsourcefile(func))))

cur_dir = get_dir(lambda:0)

# Google API (requires API key)
serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
api_key = "AIzaSyC_BCZant9pldLIVDx93xs-7jCFyn6L5Ao"
# If you are in China this URL might work (with key):
# serviceurl = "http://maps.google.cn/maps/api/geocode/json?"

#serviceurl = "http://python-data.dr-chuck.net/geojson?"


# Deal with SSL certificate anomalies Python > 2.7
# scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
scontext = None


conn = sqlite3.connect(os.path.join(cur_dir,'geodata.sqlite'))
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# fh = open(r"Python_for_Everyone_Specialty\Using_Databases_with_Python\Geocoding\where.data")
fh = open(os.path.join(cur_dir,"where.data"))
for line in fh:
    address = line.strip()
    print ()
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print ("Found in database ",address)
        continue
    except:
        pass

    print ('Resolving', address)
    url = serviceurl + urllib.parse.urlencode({"sensor":"false", "address": address})
    print ('Retrieving', url)
    req = urllib.request.Request(url, {"x-api-key": api_key} )
    # uh = urllib.request.urlopen(req, context=scontext)
    uh = urllib.request.urlopen(req)
    data = uh.read().decode()
    print ('Retrieved',len(data),'characters',data[:20].replace('\n',' '))
    try: 
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except: 
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') : 
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    cur.execute('''INSERT INTO Locations (address, geodata) 
            VALUES ( ?, ? )''', ( memoryview(address.encode()),memoryview(data.encode()) ) )
    conn.commit() 

print ("Run geodump.py to read the data from the database so you can visualize it on a map.")

import json

js = '''["Glenn","Sally","Jen"]'''

parsed = json.loads(js)

print(type(parsed), parsed)
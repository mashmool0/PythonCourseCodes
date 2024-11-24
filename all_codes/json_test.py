import json 
import requests



with open('test.json') as f  :
    data = json.load(f)



print(int(data['main']['temp'])-273,'C')
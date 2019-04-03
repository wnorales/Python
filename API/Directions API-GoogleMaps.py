import requests
import json

"""Directions"""
api_key = 'AIzaSyC5jrYNJKA0H14MUdtLsTamZup8WuN5g9Q'

url2 = "https://maps.googleapis.com/maps/api/directions/json?origin=Chicago&destination=NewYork&mode=transit Ca&key=" + api_key
#origin = "Toronto"
#destination = "Montreal"

response1 = requests.get(url2)
#print(response1.status_code)
"""""This is the same as the one below"""
response_json2 = json.loads(response1.text)
response_json1 = response1.json()

dictionaryToJson = json.dumps(response_json1)

print(response_json2)

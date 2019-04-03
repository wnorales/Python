import requests

api_key = 'AIzaSyC5jrYNJKA0H14MUdtLsTamZup8WuN5g9Q'
"""Test"""
url = url = "https://maps.googleapis.com/maps/api/geocode/json?address=Orlando, Ca&key=" + api_key

response = requests.get(url)
print(response.status_code)

response_json = response.json()
print(response_json)

url2 = "https://maps.googleapis.com/maps/api/directions/json?origin=Toronto&destination=Montreal Ca&key=" + api_key
# origin = "Toronto"
# destination = "Montreal"

response1 = requests.get(url2)
print(response1.status_code)

response_json1 = response1.json()
print(response_json1)

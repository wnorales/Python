import requests # This is another type of API package

r = requests.get('https://github.com/wnorales')
if r.status_code == 200:
    print('Success')
elif r.status_code == 404:
    print('Not Found')
#print(r.headers['Content-Type'])
print(r.headers)
print(r.headers['Status'])
import urllib.request # This is one type of API package

from urllib.request import urlopen

url = urlopen("https://github.com/wnorales")
print(url)

"""Example 1"""
url1 = "https://github.com/wnorales"
request = urllib.request.Request(url1)
response = urllib.request.urlopen(request)
data_content = response.read()
print(data_content)


"""Example 2"""
url2 = urllib.request.urlopen("https://github.com/users/wnorales")
url2Read = url2.read()
print(url2Read)


from lxml import html
import requests

page = requests.get('https://en.wikipedia.org/wiki/Computer_science')
tree = html.fromstring(page.content)


# Example 1


# Example 2
__author__ = 'bigm1_000'

import urllib.request
import urllib.parse

page = urllib.request.urlopen('http://www.google.com')


html = page.read()

print(html)

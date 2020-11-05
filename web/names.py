import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
count = int(input('Enter count: ')) 
position = int(input('Enter position: '))
name = ''
while count > 0:
    for i in range(len(tags)):
        if i+1 == position:
            name = str(tags[i].get('href',None))
            html = urllib.request.urlopen(name, context=ctx).read()
            soup = BeautifulSoup(html, 'html.parser')
            tags = soup('a')
            break
    count -= 1
        
pattern = '_([A-Za-z]+)\.html'
print(re.findall(pattern, name)[0])

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import sys

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')
if len(address) > 1:
    try:
        uh = urllib.request.urlopen(address, context=ctx)
    except:
        print('URL not found')
        sys.exit(1)

    data = uh.read()
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    total = 0

    for count in counts:
        total += int(count.text)

    print(total)

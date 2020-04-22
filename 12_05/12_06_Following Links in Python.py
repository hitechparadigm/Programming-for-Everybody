# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file


# 1) extract the href= vaues from the anchor tags,
# 2) scan for a tag that is in a particular position relative to the first name in the list, follow that link and
# 3) repeat the process a number of times and report the last name you find

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
url = input('Enter - ')
count = int(input('Enter count:'))
position = int(input('Enter postion:'))
#n = count
while count > 0:
    count = count - 1
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
# Retrieve all of the anchor tags
    tags = soup('a')
    newurl = tags[position-1]
    url = newurl.get('href', None)
    print(url)

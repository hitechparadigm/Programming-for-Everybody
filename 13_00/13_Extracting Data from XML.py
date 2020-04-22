import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url = input('Enter - ')
html = urllib.request.urlopen(url).read()

stuff = ET.fromstring(html)
comments = stuff.findall('comments/comment')
print('Comments count:', len(comments))
count = 0
sum = 0

for item in comments:
    sum = sum + int(item.find('count').text)

print('Sum:',sum)

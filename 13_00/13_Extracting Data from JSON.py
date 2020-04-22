import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter - ')
html = urllib.request.urlopen(url)
data = html.read().decode()
#data = json.dumps(data, indent=4)
info = json.loads(data)

print('Retrieved', len(data), 'characters')
print('User count:', len(info))

print(info)

sum = 0

for item in info['comments']:
    #name = item['name']
    count = item['count']
    #print(name, count)

    sum = sum + int(count)

print(sum)

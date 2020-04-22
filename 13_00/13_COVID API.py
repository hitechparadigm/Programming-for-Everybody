import urllib.request, urllib.parse, urllib.error
import json
import ssl
import requests
import re


serviceurl = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "749670b692mshc866b844cf5f578p17a407jsn302c16a34850"
    }

response = requests.request("GET", serviceurl, headers=headers)
data = response.text

try:
    js = json.loads(data)
except:
    js = None


lst = list()

for i in js['response']:
    country = i['country']
    newcases = i['cases']['new']
    if newcases is None: continue
    newtup = (newcases, country)
    lst.append(newtup)



for newcases, country in lst[:20]:
    print(country, newcases)

print('========================')



#for newcases, country in lst[:10]:
#    print(country, newcases)


#print('Flipped',tmp)

#tmp = sorted(tmp)
#print('Sorted',tmp[:5])

    #for country,newcases in newtuple[:20]:
    #    print(country,newcases)

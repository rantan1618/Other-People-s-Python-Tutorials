from datetime import date
import requests
import pandas as pd


baseurl = 'https://rickandmortyapi.com/api/'

endpoint = 'character'

def main_request(baseurl, endpoint, x):
    r = requests.get(baseurl + endpoint + f'?page={x}')
    return r.json()
# print(r.json()) 

def get_pages(response):
    return response['info']['pages']

def parse_json(response):
    charlist = []
    for item in response['results']:
        char = {
            'name': item['name'],
            'no_ep': len(item['episode']),
        }
        charlist.append(char)
    return charlist
mainlist = []

data =  main_request(baseurl, endpoint, 1)
for x in range(1,get_pages(data)+1):
    print(x)
    mainlist.extend(parse_json(main_request(baseurl,endpoint, x)))
    
df = pd.DataFrame(mainlist)

print(df.head(), df.tail())    
print(len(mainlist))
# print(parse_json(data))


# name = data['results'][0]['name']

# episodes = data['results'][0]['episode']
    
# print(item['name'], len(item['episode']))
# pages = data['info']['pages']





# print(len(episodes))

# print(data['info'])
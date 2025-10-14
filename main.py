import requests, json, os

result = requests.get("https://randomuser.me/api/")

data = result.json()

#print(json.dumps(data, indent=3))

name = f'{data['results'][0]['name']['first']} {data['results'][0]['name']['last']}'

image = data['results'][0]['picture']['large']

picture = requests.get(image)

for person in data['results']:   
    f = open(f'poze/poza.jpg', 'wb')
    f.write(picture.content)
    index += 1
    f.close()
    

print(image)
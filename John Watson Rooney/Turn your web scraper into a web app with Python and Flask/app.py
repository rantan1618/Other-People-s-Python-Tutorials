from flask import Flask
from flask.templating import render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beerjson = r.json()
#
 #   print(beerjson[0]['name'])
 #   print(beerjson[0]['abv'])
 #   print(beerjson[0]['description'])
 #   print(beerjson[0]['food_pairing'][0])

    beer = {
        'name': beerjson[0]['name'],
        'abv': beerjson[0]['abv'],
        'desc': beerjson[0]['description'],
        'foodpair': beerjson[0]['food_pairing'][0]
    }
    print(beer)
    return render_template('index.html', beer=beer)



if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)


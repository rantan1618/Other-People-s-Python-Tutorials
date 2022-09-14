import requests
from bs4 import BeautifulSoup
from pony import orm

db =  orm.Database()
db.bind(provider='sqlite', filename='products.db', create_db=True)

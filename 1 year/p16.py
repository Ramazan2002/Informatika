import requests
from bs4 import BeautifulSoup

link = 'https://kazan.cian.ru/cat.php?currency=2&deal_' \
       'type=sale&engine_version=2&maxprice=4000000' \
       '&offer_type=flat&region=4777&room1=1&room2=1'

page = requests.get(link).text
soup = BeautifulSoup(page, "lxml")

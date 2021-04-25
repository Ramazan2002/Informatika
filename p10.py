import pickle
import requests
# import matplotlib.pyplot as plt

endpoint = "https://api.punkapi.com/v2/beers/"

request = f"{endpoint}?tagline=Stout&80abv_gt=3.5&abv_lt=8&ibu_gt=5&ibu_lt=80&per_page=50"

answ = requests.get(request)
k = 0
for beer in answ.json():
  print(beer)
  print("= " * 10)
  k += 1
  print(k)

import requests
import json
import csv

f = csv.writer(open("country.csv", "wb+"))
f.writerow(["player_id", "country", "gender"])

for page in range(500):
    url = 'https://x37sv76kth.execute-api.us-west-1.amazonaws.com/prod/users?page=%s'%page
    data = requests.get(url).json()
    for row in data:
        f.writerow([row['id'],row['data']['nat'],row['data']['gender']])


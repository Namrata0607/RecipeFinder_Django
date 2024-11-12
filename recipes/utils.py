# recipes/utils.py
import requests
from django.conf import settings

def get_recipes(ingredient):
    url = f'https://api.api-ninjas.com/v1/recipe?query={ingredient}'
    headers = {'X-Api-Key': settings.API_NINJAS_KEY}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

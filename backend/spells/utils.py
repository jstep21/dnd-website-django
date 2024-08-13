import requests
from django.core.cache import cache

def fetch_spell_data():
    url = 'https://dnd5eapi.co/api/spells'
    headers = {'Accept': 'application/json'}
    cached_data = cache.get('spell_data')
    if cached_data is not None:
        return cached_data
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        cache.set('spell-data', data, timeout=3600)
        return data
    else:
        return {'results': []}

from django.core.cache import cache
from django.shortcuts import render, redirect
import requests
from .utils import fetch_spell_data


def list_spells(request):
    """Renders webpage for a list of all spells."""
    spells_data = fetch_spell_data()
    spells = spells_data.get('results', [])
    return render(request, 'spell-list.html', {'spells': spells})


def search_spells(request):
    """Search for matching spell and render spell search page"""
    user_spell = request.GET.get('search_spell', '').strip()
    if not user_spell:
        return redirect('home')
    
    spells_data = fetch_spell_data()
    spells = spells_data.get('results', [])
    
    user_spell_normalized = user_spell.lower()
    matching_spell = next((spell for spell in spells if spell['name'].lower() == user_spell_normalized), None)
    
    if matching_spell:
        spell_url = matching_spell['url'].replace(' ', '%20')
        search_response = requests.get(f'https://dnd5eapi.co{spell_url}', headers={'Accept': 'application/json'})
        spell_data = search_response.json() if search_response.status_code == 200 else {}
        
        classes = [dnd_class for dnd_class in spell_data.get('classes', [])]
        return render(request, 'spell-search.html', {
            'spell_data': spell_data,
            'user_spell': user_spell,
            'classes': classes
        })
    else:
        return redirect('home')
        
        
        
        

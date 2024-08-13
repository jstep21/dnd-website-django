from django.shortcuts import render
import requests
from django.conf import settings

def class_info(request, class_name):
    """Render webpage for class data"""
    class_resources = []
    url = f'{settings.API_BASE_URL}/classes/{class_name}/levels'
    headers = {'Accept': 'application/json'}
    
    response = requests.get(url=url, headers=headers)
    
    if response.status_code == 200:
        class_resources = response.json()
        
    return render(request, 'class-info.html', {
        'class_name': class_name,
        'class_resources': class_resources
    })
        

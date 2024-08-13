from django.urls import path
from . import views

urlpatterns = [
    path('list-spells/', views.list_spells, name='list_spells'),
    path('search-spells/', views.search_spells, name='search_spells')
]

from django.urls import path
from . import views

urlpatterns = [
    path('<str:class_name>/', views.class_info, name='class_info')
]

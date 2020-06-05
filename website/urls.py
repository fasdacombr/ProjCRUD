# Importamos a função index() definida no arquivo views.py
from django.urls import path
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # Get /
    path('', views.index, name='index'),
]
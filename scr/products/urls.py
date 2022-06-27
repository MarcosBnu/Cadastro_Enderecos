from django.urls import path
from .views import list_pessoa, create_pessoa

urlpatterns = [
    path('new', create_pessoa, name='create_pessoas'),
    path('', list_pessoa, name='list_pessoas'),
]
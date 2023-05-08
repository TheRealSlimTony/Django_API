from .views import PokemonView,home
from django.urls import path 
from Proyecto_API import views as h


urlpatterns = [

    path('api/pokemons/', PokemonView.as_view(), name='pokemons_list'),



]

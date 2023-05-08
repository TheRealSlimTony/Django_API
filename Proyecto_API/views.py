from django.shortcuts import render
from django.views import View
from .models import Pokemon


class PokemonView(View):
    def get(self, request):
        pokemon = pokemon.objects.all()

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


def home(request):
    return render(request, 'home.html')
import folium

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime
from django.core.exceptions import ObjectDoesNotExist


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    print(image_url)
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        if pokemon.image:
            image_url = request.build_absolute_uri(pokemon.image.url)
        else:
            image_url = ''
        for pokemon_entity in PokemonEntity.objects.filter(
                pokemon=pokemon,
                appeared_at__lt=localtime(),
                disappeared_at__gt=localtime(),
        ):
            add_pokemon(
                folium_map,
                pokemon_entity.latitude,
                pokemon_entity.longitude,
                image_url,
            )

    pokemons_on_page = []
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        requested_pokemon = Pokemon.objects.get(id=pokemon_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    pokemon_on_page = {
        'pokemon_id': requested_pokemon.id,
        "title_ru": requested_pokemon.title_ru,
        "title_en": requested_pokemon.title_en,
        "title_jp": requested_pokemon.title_jp,
        "description": requested_pokemon.description,
        "img_url": requested_pokemon.image.url if requested_pokemon.image else '',
    }

    if requested_pokemon.next_evolution:
        pokemon_on_page['next_evolution'] = {
            "title_ru": requested_pokemon.next_evolution.title_ru,
            "pokemon_id": requested_pokemon.next_evolution.id,
            "img_url": requested_pokemon.next_evolution.image.url
            if requested_pokemon.next_evolution.image else ''
        }

    if requested_pokemon.previous_evolution:
        pokemon_on_page['previous_evolution'] = {
            "title_ru": requested_pokemon.previous_evolution.title_ru,
            "pokemon_id": requested_pokemon.previous_evolution.id,
            "img_url": requested_pokemon.previous_evolution.image.url
            if requested_pokemon.previous_evolution.image else ''
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in PokemonEntity.objects.filter(
            pokemon=requested_pokemon,
            appeared_at__lt=localtime(),
            disappeared_at__gt=localtime(),
    ):
        if requested_pokemon.image:
            image_url = request.build_absolute_uri(requested_pokemon.image.url)
        else:
            image_url = ''
        add_pokemon(
            folium_map,
            pokemon_entity.latitude,
            pokemon_entity.longitude,
            image_url,
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_on_page
    })

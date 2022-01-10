#!/usr/bin/env python3
"""Final project for Alta Labs Python Class 9 Jan 2022
   Project written by Michael Stack github: https://github.com/AgentKD6-37
   This program is the PokeDex! It takes a user input on what Pokemon they see and returns the Pokemon's info from
   https://pokeapi.co for usage see the repo license"""

import json
from random import randint

import requests

API_Pokemon = f"https://pokeapi.co/api/v2/pokemon/"
API_Species = f"https://pokeapi.co/api/v2/pokemon-species/"


def start_pokedex():
    print("Pokedex v1.0 is starting up!")
    user_input = input("What Pokemon would you like to identify? \n").lower()
    return user_input


def get_pokemon(pokemon):
    if pokemon:
        poke_url = API_Pokemon + pokemon + "/"
        poke_data = requests.get(poke_url).json()
        poke_id = str(poke_data["id"])
        species_data = requests.get(API_Species + poke_id + "/").json()
        species_data.update(poke_data)
    else:
        start_pokedex()
    return species_data


def pretty_response(data):
    random_flavor_text = randint(0, 15)
    if data:
        pokemon_name = data["name"].capitalize()
        pokemon_type = data["types"][0]["type"]["name"].capitalize()
        pokemon_height = data["height"]
        pokemon_weight = (data["weight"]) / 10
        pokemon_color = data["color"]["name"]
        pokemon_flavor_text = data["flavor_text_entries"][random_flavor_text]["flavor_text"]
        print(
            f"{pokemon_name} is a {pokemon_type}-Type Pokemon. Commonly {pokemon_height}m tall and weighing on"
            f" average {pokemon_weight}kg. This pokemon is {pokemon_color} in color. \n"
            f"{pokemon_flavor_text}"
        )


def main():
    user_input = start_pokedex()
    data = get_pokemon(user_input)
    pretty_response(data)


main()

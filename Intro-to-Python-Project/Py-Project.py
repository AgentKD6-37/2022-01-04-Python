#!/usr/bin/env python3
"""Final project for Alta Labs Python Class 9 Jan 2022
   Project written by Michael Stack github: https://github.com/AgentKD6-37
   This program is the PokeDex! It takes a user input on what Pokemon they see and returns the Pokemon's info from
   https://pokeapi.co for usage see the repo license"""
import requests

API = f"https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(pokemon):
    if pokemon:
        url = API + pokemon + "/"
        data = requests.get(url)
    return data

def pretty_response(pokemon):
    return

def main():
    print("Pokedex v1.0 is starting up!")
    user_input = input("What Pokemon would you like to identify").lower()
    data = get_pokemon(user_input)
    print(data.json())

main()
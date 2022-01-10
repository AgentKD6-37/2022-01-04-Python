#!/usr/bin/env python3
"""Final project for Alta Labs Python Class 9 Jan 2022
   Project written by Michael Stack github: https://github.com/AgentKD6-37
   This program is the PokeDex! It takes a user input on what Pokemon they see and returns the Pokemon's info from
   https://pokeapi.co for usage see the repo license"""

from random import randint
import config
import requests


def start_pokedex():
    """This function starts the pokedex, greets the user, and takes and then returns the user input to main
    for manipulation"""
    input("Pokedex v1.0 is starting! Press Enter to continue...")
    user_input = input("\n\n\nWhat Pokemon would you like to identify: ").lower()
    return user_input


def get_pokemon_picture(picture_url):
    """This function uses the filestack api to take the image sprite returned from the JSON data from pokeapi and
    transforms it into ASCII text art that is then stripped of it's html headers, spaced for python, and printed to the
    console"""
    ascii_maker_api = f"https://process.filestackapi.com/{config.API_KEY}/ascii/{picture_url}"
    poke_picture = requests.get(ascii_maker_api)
    poke_picture_ascii = poke_picture.text.replace("<br>", "\n")
    poke_picture_ascii_no_header = poke_picture_ascii.replace('<html><head></head><body style="background: #FFFFFF"><pre style="font-family: Consolas, monaco, monospace; font-size: 12px; color: #000000">', "")
    poke_picture_ascii_no_footer = poke_picture_ascii_no_header.replace('</pre></body></html>', "")
    print(poke_picture_ascii_no_footer)


def get_pokemon(pokemon):
    """This function takes the user input 'pokemon' and returns the JSON data from the API call to main."""
    if pokemon:
        try:
            poke_url = config.API_Pokemon + pokemon + "/"
            poke_data = requests.get(poke_url).json()
            poke_id = str(poke_data["id"])
            species_data = requests.get(config.API_Species + poke_id + "/").json()
            species_data.update(poke_data)
        except:
            input("There was no result for that pokemon! To try again press Enter")
            main()
    else:
        start_pokedex()
    return species_data


def pretty_response(data):
    """This function exists to parse JSON data of different pokemon and pull the relevant stats to be displayed to
    the user. It then prints the info to console for the user to read."""
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
            f"\n"
            f"\n"
        )


def results_selection():
    """This function allows the script to loop and be run again or to quit."""
    user_choice = input("Would you like to search another (p)okemon or (q)uit? \n "
                        "please type p to search another pokemon or q to quit: ").lower()
    if user_choice == "p":
        main()
    elif user_choice == "q":
        return
    else:
        print("invalid! please type p to search another pokemon or q to quit.")
        results_selection()


def main():
    """Main method, pretty straight-forward. It runs the functions in order to generate results for the user."""
    user_input = start_pokedex()
    data = get_pokemon(user_input)
    get_pokemon_picture(data["sprites"]["front_default"])
    pretty_response(data)
    results_selection()

main()
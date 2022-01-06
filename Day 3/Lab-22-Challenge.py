#!/usr/bin/env python3

def main():
    """Solution by myself. Drill down into each dictionary, check if the item is a farm name, if so: print it! if not,
    we save the value of the item as a new var, then loop through that list"""


    farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
             {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
             {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
    for farm in farms:
        for item in farm:
            if item == "name":
                print(farm[item])
            else:
                aglist = farm[item]
                for i in aglist:
                    print(i)
        print("----------------")


main()
#!/usr/bin/env python3

def main():
    """If the hostname is MTG, it should tell you. Else it will exit early."""
    hostname = input("What value should we set for hostname?")
    ## Notice how the next line has changed
    ## here we use the str.lower() method to return a lowercase string
    if hostname.lower() == "mtg":
        print("The hostname was found to be mtg")
        print("hostname matches expected config")
    print("exiting the script")

main()

#!/usr/bin/env python3

def main():
    print("Welcome to the network grader!")
    user_input = input("How fast is your wi-fi network? \n(answers must be a number from 1MBPS to 1000MPS for gigabyte and above speeds)\n")
    int_user_input = int(user_input)

    if int_user_input >= 1000:
        print("Your Wi-fi is grade S! Fantastic!")
    elif int_user_input >= 500:
        print("Your Wi-fi is grade A. Pretty Fast, but not the best.")
    elif int_user_input >= 200:
        print("Your Wi-fi is grade B. Quick but definitely could be better.")
    elif int_user_input >= 100:
        print("Your Wi-fi is grade C. You might need an upgrade.")
    elif int_user_input >= 50:
        print("Your Wi-fi is grade D. Do you live in the country?")
    else:
        print("Your Wi-fi is grade F! Oh no!")

if __name__ == "__main__":
    main()

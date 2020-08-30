"""
CP1404/CP5632 - assignment_01
Travel Tracker

Daniel Mackenzie
"""

MENU = "Menu:\nL - List places\nA - Add new place\nM - Mark a place as visited\nQ - Quit\n>>> "


def main():
    places = get_places()
    print(places)
    print_welcome_msg()
    get_choices = input("MENU")
    while get_choices != "Q":
        if get_choices == "L":
            pass
        elif get_choices == "A":
            pass
        elif get_choices == "M":
            pass
        else:
            print("Invalid menu choice")
        get_choices = input("MENU")


def get_places():
    in_file = open("places.csv", 'r')
    places = in_file.read().strip()
    in_file.close()
    return places


def print_welcome_msg():
    print("Travel Tracker 1.0 - by Daniel Mackenzie\n"
          f"places loaded from places.csv")




main()
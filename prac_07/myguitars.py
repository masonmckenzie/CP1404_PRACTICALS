"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
import csv
from prac_07.myguitars import guitars


def main():
    """The program below Guitar program, with implemented Guitar class."""
    guitars = []

    print("my guitars:")
    name = input("name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:  # The if statement contains lists and strings, for True when non-empty
        guitars.sort()
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))
    else:
        print("You have zero guitars. How about you get a new one ?????")


main()
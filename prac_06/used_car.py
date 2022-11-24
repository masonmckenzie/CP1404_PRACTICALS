"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from prac_06.car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"


def main():
    """Car simulation program, showing use of Car class."""
    print("Let's drive!")
    name = input("Enter your car name: ")
    # create a Car instance with initial fuel of 100 and user-provided name
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(
                input("How many km do you want to drive? "))
            while distance_to_drive < 0:
                print("Distance must be greater than 0")
                distance_to_drive = int(
                    input("How many km do you want to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print(f"The car drove {distance_driven}km", end="")
            if car.fuel == 0:
                print(" and ran out of fuel", end="")
            print(".")
        elif choice == "r":
            fuel_to_add = int(input("How much fuel do you want to add to the car? "))
            while fuel_to_add < 0:
                print("Fuel amount must be greater than 0")
                fuel_to_add = int(input("How much fuel do you want to add to the car? "))
            car.add_fuel(fuel_to_add)
            print(f"Added {fuel_to_add} units of fuel.")
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print(f"\nGood bye {car.name}'s driver.")


main()


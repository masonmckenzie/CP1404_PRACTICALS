"""
CP1404/CP5632 Practical
Mason McKenzie
"""


from prac_09.unreliable_car import UnreliableCar


def main():
    """testing the unreliability car class"""
    car_1 = UnreliableCar("consistently reliable car", 200, 100)
    car_2 = UnreliableCar("largely reliable car", 200, 75)
    car_3 = UnreliableCar("fifty fifty reliable car", 200, 50)
    car_4 = UnreliableCar("largely reliable car", 200, 25)
    car_5 = UnreliableCar("consistently reliable car", 200, 0)

    for i in range(5):
        print(f"test {i + 1}\n")
        print(f"{car_1.name} has driven {car_1.drive(20)}km")
        print(f"{car_1}\n")
        print(f"{car_2.name} has driven {car_2.drive(20)}km")
        print(f"{car_2}\n")
        print(f"{car_3.name} has drive {car_3.drive(20)}km")
        print(f"{car_3}\n")
        print(f"{car_4.name} has driven {car_4.drive(20)}km")
        print(f"{car_4}\n")
        print(f"{car_5.name} has driven {car_5.drive(20)}km")
        print(f"{car_5}\n")


main()

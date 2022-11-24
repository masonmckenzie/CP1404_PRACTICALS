"""
CP1404/CP5632 Practical
Mason McKenzie
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test luxury Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()

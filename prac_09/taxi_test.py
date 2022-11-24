"""
CP1404/CP5632 Practical
Mason McKenzie
"""

from prac_09.taxi import Taxi

my_taxi = Taxi("PRIUS, 1", 100)
my_taxi.drive(40)
print(my_taxi)

my_taxi.start_fare()
my_taxi.drive(100)
print(my_taxi)

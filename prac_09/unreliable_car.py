"""
CP1404/CP5632 Practical
Mason McKenzie
"""


from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """subgroup class for car"""

    def __init__(self, name, fuel, reliability):
        """initialising for the not reliable car"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive is the same as the parent car however the individual reliability will control"""
        random_number = randint(0, 100)
        if random_number >= self.reliability:
            distance = 0
        distance_driven = super().drive(distance)
        return distance_driven




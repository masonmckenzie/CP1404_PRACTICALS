"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""
"""CP1404/CP5632 Practical - Car class ."""


class Car:
    """the a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialising for a Cars instance"""
        self.name = name
        self.fuel = fuel
        self._odometer = 0  # We name this with a leading _ as it is "non-public"

    def __str__(self):
        """Return a string representing the Car object."""
        return f"{self.name}, fuel={self.fuel}, odometer={self._odometer}"

    def add_fuel(self, amount):
        """Adding in the amount of fuel to the cars."""
        self.fuel += amount

    def drive(self, distance):
        """Drives the car certain distance.
        Drives a certain distance if the car has enough fuel
        or until fuel runs out gives back the distance driven.
        """
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self._odometer += distance
        return distance


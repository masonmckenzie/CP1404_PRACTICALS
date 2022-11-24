"""
CP1404/CP5632
Mason McKenzie
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.5

    def __init__(self, name, fuel, embellishment):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.embellishment = embellishment
        self.price_per_km *= embellishment

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Get the fare."""
        return self.flagfall + super().get_fare()

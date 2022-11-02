"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
""""""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

"""Estimated time to complete -- 1hr
Time to complete -- 42min"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50


class Guitar:
    """Guitar class used to store details of the guitars."""
    def __init__(self, name="", year=0, cost=0):
        """Initialising the Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the string representation for the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Get the age of a guitar based on the "CURRENT_YEAR"."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the Guitar is considered vintage or not ."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Less than, used for sorting Guitars - by year of release."""
        return self.year < other.year


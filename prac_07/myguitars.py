"""
CP1404/CP5632 Practical
Mason McKenzie
note that for the below code to save space the prac_06 could have been
used to import guitars.py, however if the individual didn't also have this
folder then the code would not run correctly so it made sense to include the
code (functions) in this code as well so users won't have there list affected
"""


import csv

## it's best to put this in the physical code, because if someone doesn't have the guitars folder then they wont be able to reference the functions from the code
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

def main():
    guitars = get_guitars()
    for guitar in guitars:
        print(guitar)

def get_guitars():
    guitars = []
    with open('guitars.csv', 'r', newline='') as in_file:
        in_file.readline()
        reader = csv.reader(in_file)
        for row in reader:
            guitar = Guitar(row[0], row[1], float(row[2]))
            guitars.append(guitar)
        guitars.sort()
    in_file.close()
    return guitars

main()




# import datetime
#
# date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
# date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
# print(f"That day is/was {date.strftime('%A')}")
# print(date.strftime("%d/%m/%Y"))

class ProjectManagement:
    """Represent information about a programming language."""

    def __init__(self, name, date, priority, cost, completion):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.date} date, priority={self.priority}, cost Arithmetic={self.cost}, First appeared in {self.completion}"



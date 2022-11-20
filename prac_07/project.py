
"""
CP1404/CP5632 Practical
Mason McKenzie
"""


import csv
from collections import namedtuple

from project_management import ProjectManagement

class Project:
    def __init__(self, name, date, priority, cost, percentage):
        self.name = name
        self.start_date = date
        self.priority = priority
        self.cost = cost
        self.percentage = percentage

    def __lt__(self, other):
        return self.priority < other.priority

    def __str__(self):
        return f"{self.name}\t{self.start_date.strftime('%date/%month/%Year')}\t{self.priority}\t{self.cost}\t{self.percentage}"



    def project_finished(self):
        return self.percentage == 100
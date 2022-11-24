"""
CP1404/CP5632 Practical
Mason McKenzie
"""



class Band():

    def __init__(self, name=" "):
        self.musicians = []
        self.name = name

    def __str__(self):
        return {self.name}, ({''.join([musician.__str__() for musician in self.musicians])})

    def played_band(self):
        return '\n'.join([musician.play() for musician in self.musicians])

    def add_member(self, musician):
        self.musicians.append(musician)

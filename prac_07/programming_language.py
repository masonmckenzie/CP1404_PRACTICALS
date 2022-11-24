"""
CP1404/CP5632 Practical
Mason McKenzie
"""


class ProgrammingLanguage:
    """shows the information for the programming language."""

    def __init__(self, name, typing, reflection, pointer, year):
        """use the values below to make a language"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer = pointer
        self.year = year

    def is_dynamic(self):
        """find out if the language is dynamically typed."""
        return self.typing == "is dynamically typed"
    def __repr__(self):
        """Returns the string for programming language."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, Pointer Arithmetic={self.pointer}, First appeared in {self.year}"




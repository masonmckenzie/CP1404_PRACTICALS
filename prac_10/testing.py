"""
CP1404/CP5632
convert_miles_km
Mason McKenzie
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeats a string of s, a number of times n."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("nothing")
    False
    >>> is_long_word("mother")
    True
    >>> is_long_word("racecar", 7)
    True
    """
    return len(word) >= length


def run_tests():
    """Runs tests on functions."""
    # assert test without message
    assert repeat_string("Python", 1) == "Python"
    # this test will be a fail
    assert repeat_string("hi", 2) == "hi hi"

    # 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car doesn't set odometer correctly"

    # 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these

    # Test value that's passed in
    test_car = Car(fuel=10)
    assert test_car.fuel == 10

    # Test the default
    test_car = Car()
    assert test_car.fuel == 0


run_tests()

# 3. Uncomment the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# 4. Fix the failing is_long_word function
# (don't change the tests, change the function!)

# 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass

def format_phrase_to_sentence(phrase):
    """formats a sentence from the phrase."""
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


assert format_phrase_to_sentence('hello') == 'Hello.'
assert format_phrase_to_sentence('It is an ex parrot.') == 'It is an ex parrot.'
assert format_phrase_to_sentence('i like movies.') == 'I like movies.'

"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return s * n


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) > length


def run_tests():
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"
    test_car = Car(fuel=10)
assert Car(fuel=10)

run_tests()

 doctest.testmod()


phrase= input("What phrase do you want formating")
print(phrase,"2f ..")
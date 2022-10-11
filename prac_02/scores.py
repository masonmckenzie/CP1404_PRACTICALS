"""
CP1404/CP5632 - Practical - Mason McKenzie
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    get_grade(score)


def get_grade(score):
    if score < 0:
        print("Invalid score")
    elif score < 50:
        print("Bad")
    elif score < 90:
        print("Pass")
    elif score <= 100:
        print("Excellent")
    else:
        print("Invalid score")


main()

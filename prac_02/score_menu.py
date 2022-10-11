"""
CP1404/CP5632 - Practical - Mason McKenzie
Score menu
"""


def main():
    score = get_valid_score()
    get_grade(score)
    print_asterisks(score)


def get_valid_score():
    score = int(input("Score: "))
    while 0 > score > 100:
        score = int(input("Score: "))
    return score


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


def print_asterisks(score):
    for i in range(score):
        print("*", end="")


main()
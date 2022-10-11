"""
CP1404/CP5632 - Practical - Mason McKenzie
More scores
"""
import random


def main():
    number_of_scores = int(input("Number of scores? "))
    file1 = open("results.txt", "w")
    for i in range(number_of_scores):
        score = random.randint(0, 100)
        grade = get_grade(score)
        print(f"{score} is {grade}", file=file1)
    file1.close()
    print(f"Printed {number_of_scores} numbers to results.txt")


def get_grade(score):
    if score < 0:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Pass"
    elif score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


main()
"""
CP1404/CP5632 Practical - Mason McKenzie
list_exercises
"""

def main():
    numbers = []
    for i in range(5):
        number = int(input("numbers: "))
        numbers.append(number)
    number_details(numbers)


def number_details(numbers):
    print(f"the first number is {numbers[0]}")
    print(f"the second number is {numbers[-1]}")
    print(f"the smallest number is {min(numbers)}")
    print(f"the biggest number is {max(numbers)}")
    print(f"the average number is {(sum(numbers))/(len(numbers))}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")

main()



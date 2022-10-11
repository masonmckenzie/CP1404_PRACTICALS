"""
CP1404/CP5632 - Practical - Mason McKenzie
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished = True  # 'is_finished = ture' was the segment added so could return true
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
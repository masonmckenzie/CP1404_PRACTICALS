"""
CP1404/CP5632 - Practical - Mason McKenzie
Quick file opening/writing/reading exercises
"""

# Program 1 - open and write in name.txt
out_file = open("name.txt", "w")  # to open and write in name.txt document
name = input("Input user name? ")
print(name, file=out_file)  # or out_file.write(name)
out_file.close()

# Program 2 - open and read name.txt to find name using with
with open("name.txt", "r") as in_file:
    name = in_file.read().strip()
print("Your name is", name)


# Program 3 - open and read name.txt to find username
in_file = open("name.txt", "r")  # to read the opened file
name = in_file.read().strip()
in_file.close()
print("User name is", name)

# Program 4 - printing number one and two from numbers.txt file
in_file = open("numbers.txt", "r")
number_one = int(in_file.readline())  # int() is used to handle whitespace
number_two = int(in_file.readline())  # int() is used to handle whitespace
in_file.close()
print(number_one + number_two)

# summing of all numbers
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
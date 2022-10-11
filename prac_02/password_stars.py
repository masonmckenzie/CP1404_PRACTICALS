"""
CP1404/CP5632 - Practical - Mason McKenzie
Password stars
"""
MINIMUM_LENGTH = 5


def main():
    """Main program."""
    password = get_password()
    prints_asterisks(password)


def prints_asterisks(password):
    for char in password:
        print("*", end="")


def get_password():
    """Get a valid password."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password needs to be atleast {MINIMUM_LENGTH} characters")
        password = input("Enter password: ")
    return password


main()
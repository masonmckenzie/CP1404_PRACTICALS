"""
CP1404/CP5632 - Practical - Mason McKenzie
"""
# setting constants
minimum_length = 2
maximum_length = 6
SPECIAL_CHARS_REQUIRED = False  # special characters aren't needed
special_characters = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """getting and checking password of user"""
    print("Enter a valid password")
    print("User password must be between", minimum_length, "and", maximum_length,
          "characters, and contain:")
    print("\t1 or more uppercase letters")
    print("\t1 or more lowercase letters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", special_characters)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password not valid: " + password)

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # counting the different characters e.g. upper, lower special characters
        if char.isdigit():
            count_digit += 1
        elif char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char in special_characters:
            count_special += 1

    # returning false for normal counts of zero
    if count_lower == 0 or count_digit == 0 or count_upper == 0:
        return False

    # amount of special_characters required
    if SPECIAL_CHARS_REQUIRED:
        if count_special == 0:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


def is_valid_password(password):
    """validating password"""
    if len(password) < minimum_length or len(password) > maximum_length:
        return False


main()
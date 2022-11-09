import csv
from collections import namedtuple

from project_management import ProjectManagement

def main():
    projects = []

    # opening the file in read mode
    my_file = open("projects.txt", "r")

    # reading the file
    data = my_file.read()

    # replacing end of line('/n') with ' ' and
    # splitting the text it further when '.' is seen.
    data_into_list = data.replace('\n', ' ').split(".")

    # printing the data
    print(data_into_list)
    my_file.close()
    # Close the file as soon as we've finished reading it
    # Loop through and display all languages (using their str method)
    # for project in projects:
    #     print(project)
def menu():
    print(f"Menu: \n{'(L)oad Projects'} \n{'(S)ave Projects'} \n{'(D)isplay Projects'} \n{'(F)ilter Projects by date'} \n{'(A)dd Project'} \n{'(U)pdate Project'} \n{'(Q)uit'}")
    option = input(">>>").upper()
    if option == "L":
        print("You have chosen Load")
        main()
    elif option == "S":
        print("You have chosen Save")
    elif option == "D":
        print("You have chosen Display")
    elif option == "F":
        print("You have chosen Filter")
    elif option == "A":
        print("You have chosen Add")
    elif option == "U":
        print("You have chosen Update")
    elif option == "Q":
        print("You have chosen Quit")
    else:
        print("Please choose valid option")

menu()

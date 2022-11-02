"""
ASSIGNMENT_1_CP1404
Name: Mason McKenzie
Date started: 24/10/22
GitHub URL: https://github.com/cp1404-students/a1-movies-masonmckenzie
"""
from operator import itemgetter
import csv

FILENAME = "movies.csv"


def main():
    in_file = open("movies.csv")
    print("Welcome to Movies To Watch 1.0 \nBy MASON MCKENZIE")
    records = get_records(FILENAME)
    new_csv = records.copy()
    draft_csv = new_csv.copy()
    give_placement(new_csv)
    menu(new_csv, draft_csv)



def menu(new_csv, draft_csv):
    """The menu function allow the user to view the options avaliable"""
    print(f"Menu: \n{'1.Display (D)'} \n{'2.Add (A)'} \n{'3.Watch (W)'} \n{'4.Quit (Q)'}")
    option = input("What would you like to choose today?: ").upper()
    if option == "D":
        print("You have chosen display")
        display_movies(new_csv, draft_csv)
    elif option == "W":
        print("You have chosen watch")
        check_movies(new_csv, draft_csv)
    elif option == "A":
        print("You have chosen add")
        add_movies(new_csv, draft_csv)
    elif option == "Q":
        print("You have chosen quit")
        print(draft_csv)
        commit_to_csv(draft_csv)
    else:
        print("Pick a valid option")
        menu(new_csv, draft_csv)


def get_records(filename):
    """makes the file a list"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
        sort_data(records)
    return records


def give_placement(new_csv):
    """Gives the movies a place holder number"""
    placement = 0
    for data in new_csv:
            placement = placement + 1
            data.append(placement)


def back_to_menu(new_csv, draft_csv):
    """Takes the user back to the menu"""
    back = input('Press the "B" button to return to the menu: ').upper()
    while back != "":
        if back == "B":
            menu(new_csv, draft_csv)
        else:
            print("Invalid Action")
        back = input('Press the "B" button to return to the menu: ').upper()


def display_movies(new_csv, draft_csv):
    """the functions is used to show the movies in a list thats orders as well as informing the user on how many are still to watch"""
    counter = 0
    for data in new_csv:
        if data[3] == "u":
            counter = counter + 1
            print(f"{data[4]}. {data[0]:35} - {data[1]:4} - {data[2]} *")
        else:
            print(f"{data[4]}. {data[0]:35} - {data[1]:4} - {data[2]}")
    print(f"You have {counter} movie(s) left to watch")
    back_to_menu(new_csv, draft_csv)


def add_movies(new_csv, draft_csv):
    """this function consists of two parts, firstly it will add the movie to the list, and secondly acts as an error checker for the user inputs"""
    movie_addition = []  # setting movie additions variable to a list, that will then be updated
    movie_name = input("input the year of release: ")
    while movie_name == "":
        print("A name is required")  # when a black input occurs
        movie_name = input("input the year of release: ")
    movie_addition.append(movie_name)  # to show movie associated with the year
    print("Title:", movie_name)
    movie_year = (input("input the year of release: "))
    while not movie_year.isdigit():
        print("A name is required")
        movie_year = (input("input the year of release: "))
    else:
        movie_year = int(movie_year)
        while movie_year <= 0:
            print("Year must be >= 1")
            movie_year = int(input("input the year of release: "))
        else:
            movie_addition.append(movie_year)
            print("Year: ", movie_year)
    genre_options = ['ACTION', 'COMEDY', 'DOCUMENTARY', 'DRAMA', 'THRILLER', 'OTHER']
    genres = ' '.join(['Action,', 'Comedy,', 'Documentary,', 'Drama,', 'Thriller,', 'Other'])
    print("These are the Genre's in the list:", genres)
    movie_genre = input("Please input the genre you'd like to watch: ").upper()
    if movie_genre in genre_options:
        print("Genre: ", movie_genre)
        movie_addition.append(movie_genre)
    else:
        print("This genre isn't in the list, pick another")
        movie_addition.append('Other')
    print(f"{movie_addition[0]} ({movie_addition[2]} from {movie_addition[1]}) added to the movie list")
    movie_addition.append('w')
    new_csv.append(movie_addition)
    draft_csv = new_csv.copy()
    back_to_menu(new_csv, draft_csv)


def check_movies(new_csv, draft_csv):
    """this function finds out wether or not the movie has been viewed"""
    count = 0
    for data in new_csv:
        if data[3] == "u":
            count += 1
    if count > 0:
        watch_movies(new_csv, draft_csv)
    else:  # this else is for when all films have been watched, and no more to view
        print("there are no more movies to view")
        back_to_menu(new_csv, draft_csv)


def watch_movies(new_csv, draft_csv):
    """this function will allow the individual watch a movie from the movies.csv list"""
    print(new_csv)
    repeat_var = 0
    while repeat_var == 0:  # this is to only occur when the repeat_var variable is equal to zero
        movie_number = input("Choose a movie that you would like to view: ")
        if movie_number.isdigit():
            movie_number = int(movie_number)  #int means to make sure and interger is used as in 1,2,3...etc
            try:
                if 'u' in (new_csv[movie_number - 1]):
                    new_csv[movie_number - 1][3] = 'w'
                    draft_csv[movie_number - 1][3] = 'w'
                    print(f"{new_csv[movie_number - 1][0]} this movie has been watched")
                    repeat_var += 1
                    back_to_menu(new_csv, draft_csv)
                elif 'w' in (new_csv[movie_number - 1]):  # using the w to indicate the movie in question has already been watched
                    print(f"{new_csv[movie_number - 1][0]} you've already watched this")
            except IndexError:
                print("That movie does not exist") # incase and index error occurs user will see this (type in something that dose not exist
        else:
            print("Please enter a valid number")


def commit_to_csv(draft_csv):
    """commiting the changes made with the menu to the movies into the csv"""
    with open('movies_backup.csv', 'w') as file:
        writer = csv.writer(file)
        for row in draft_csv:
            print(row)
            writer.writerow(row)
    quit()

def sort_data(records):
    """the lambda function is used to sort the movies into years and then titles """
    records.sort(key=lambda x: x[0])
    records.sort(key=lambda x: int(x[1]))
    return records



main()
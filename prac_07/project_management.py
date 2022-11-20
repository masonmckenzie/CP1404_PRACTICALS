"""
CP1404/CP5632 Practical
Mason McKenzie
"""
from prac_07.project import Project
from datetime import datetime

FILENAME = "projects.txt"
TITLE = "Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage"


def main():
    projects = load_data(FILENAME)
    menu()
    command = input(">> ").upper()
    while command != 'Q':
        if command == "L":
            file_name = input("File Name: ")
            projects = load_data(file_name)
        elif command == "S":
            file_name = input("File Name: ")
            save_data(file_name, projects)
        elif command == "D":
            display(projects)
        elif command == "F":
            date = datetime.strptime(input("Projects that start after date (dd/mm/yyyy): "), '%d/%m/%Y')
            filter_projects(projects, date)
        elif command == "A":
            projects.append(add_project())
        elif command == "U":
            projects = update(projects)
        else:
            print("Bad Command")
        menu()
        command = input("> ").upper()
    print("Thank you for using custom-built project management software.")


def menu():  # Space at start to make console more readable
    print("""
L: LOAD
S: SAVE
D: DISPLAY
F: FILTER
A: ADD
U: UPDATE
Q: QUIT """)


def load_data(file_name):
    file_handler = open(file_name, 'r')
    file_handler.readline()  # Clears Header
    data = []
    for line in file_handler:
        parts = line.strip().split("\t")
        data.append(
            Project(parts[0], datetime.strptime(parts[1], "%d/%m/%Y"), int(parts[2]), float(parts[3]), int(parts[4])))
    file_handler.close()
    return data


def save_data(file_name, data):
    file_handler = open(file_name, 'w')
    print(TITLE, file=file_handler)
    for entry in data:
        print(f"{entry}", file=file_handler)
    file_handler.close()
    print(f"Data saved to: {file_name}")


def display(projects):
    print("Projects not completed:")
    incomplete_projects = [project for project in projects if not project.project_finished()]
    incomplete_projects.sort()
    for project in incomplete_projects:
        print_formatted(project)
    print("Projects completed:")
    complete_projects = [project for project in projects if project.project_finished()]
    complete_projects.sort()
    for project in complete_projects:
        print_formatted(project)


def filter_projects(projects, date):  # Sort by date
    filtered_projects = [project for project in projects if project.begining_date >= date]
    filtered_projects.sort(key=lambda x: x.begining_date)
    for project in filtered_projects:
        print_formatted(project)


def add_project():
    name = input("Project Name: ")
    date = datetime.strptime(input("Start Date (dd/mm/yyyy): "), "%d/%m/%Y")
    priority = int(input("Priority: "))
    cost = float(input("Cost Est: ").strip('$'))
    percentage = int(input("Percentage Completed: "))
    project = Project(name, date, priority, cost, percentage)
    return project

def in_range(choice, length):
    if choice < 0:
        print("!!Invalid Selection!!")
        return False
    elif choice > length - 1:
        print("!!Invalid Selection!!")
        return False
    else:
        return True


def update(projects):
    for index, project in enumerate(projects):
        print(index, end='')
        print_formatted(project)

    try:
        project_choice = int(input("Project Choice: "))
    except ValueError:
        project_choice = -1
    while not in_range(project_choice, len(projects)):
        try:
            project_choice = int(input("Project Choice: "))
        except ValueError:
            project_choice = -1

    print_formatted(projects[project_choice])
    new_percentage = input("New percentage: ")
    new_priority = input("New Priority: ")
    try:
        projects[project_choice].percentage = int(new_percentage)
    except ValueError:
        print(f"Invalid Value; Using {projects[project_choice].percentage}")
    try:
        projects[project_choice].priority = int(new_priority)
    except ValueError:
        print(f"Invalid Value; Using {projects[project_choice].priority}")
    return projects




def print_formatted(project):
    print(f" {project.name}, start: {project.begining_date.strftime('%d/%m/%Y')}, priority {project.priority}"
          f", estimate: ${project.cost}, completion: {project.percentage}%")


main()
import os
import random

class Person:
    def __init__(self, name):
        self.name = name
        self.starting_item = ""
        self.injury = ""
        self.random_item = ""
        self.random_weapon = ""

    def assign_starting_item(self):
        self.starting_item = random.choice(read_items_from_file('items.txt'))

    def assign_encounter_outcome(self):
        outcome = random.choices(['injury', 'random_item', 'random_weapon'], weights=[0.55, 0.25, 0.20])[0]

        if outcome == 'injury':
            self.injury = random.choice(read_items_from_file('injuries.txt'))
        elif outcome == 'random_item':
            self.random_item = random.choice(read_items_from_file('rand_items.txt'))
        elif outcome == 'random_weapon':
            self.random_weapon = random.choice(read_items_from_file('rand_weapons.txt'))


def read_encounters_from_file(file_path):
    with open(os.path.join('Zombie Survival Stuff', file_path), 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_items_from_file(file_path):
    with open(os.path.join('Zombie Survival Stuff', file_path), 'r') as file:
        return [line.strip() for line in file.readlines()]

def read_names_from_file(file_path):
    with open(os.path.join('Zombie Survival Stuff', file_path), 'r') as file:
        return [line.strip() for line in file.readlines()]

def generate_teams(num_teams, people_per_team):
    teams = []
    names = read_names_from_file('people.txt')
    names_list = list(names)

    while len(names_list) >= people_per_team:
        team = random.sample(names_list, people_per_team)
        people = []
        for person_name in team:
            person = Person(person_name)
            person.assign_starting_item()
            person.assign_encounter_outcome()
            people.append(person)
            names_list.remove(person_name)
        teams.append(people)

    if names_list:
        new_team = [Person(name) for name in names_list]
        for person in new_team:
            person.assign_starting_item()
            person.assign_encounter_outcome()
        teams.append(new_team)

    return teams



def print_team_status(teams):
    for team_id, team in enumerate(teams, start=1):
        print(f"Team {team_id}:")
        for person in team:
            print(f"{person.name} - Starting Item: {person.starting_item}")
            if person.injury:
                print(f"Injury: {person.injury}")
            if person.random_item:
                print(f"Random Item: {person.random_item}")
            if person.random_weapon:
                print(f"Random Weapon: {person.random_weapon}")
        print("\n")


# Read encounters, items, and names from specified files
encounters = read_encounters_from_file('encounters.txt')
items = read_items_from_file('items.txt')

# Specify the number of teams and people per team
num_teams = 11
people_per_team = 2

# Generate teams and simulate encounters
teams = generate_teams(num_teams, people_per_team)

# Print the status of each team
print_team_status(teams)



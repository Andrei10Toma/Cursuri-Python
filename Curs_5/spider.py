import requests
from bs4 import BeautifulSoup
import csv

URL = "https://lpf.ro/liga-1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results_table = soup.find(id="clasament_ajax")
team_rows = results_table.find_all(class_="echipa_row")
teams = []
for team in team_rows:
    team_cel = team.find("td", class_="echipa")
    team_name = team_cel.find("a").text.strip()
    team_position = team.find("td", class_="poz").text.strip()
    team_points = team.find("td", class_="puncte").text.strip()
    # added the number of matches played by every team
    team_played_games = team.find_all("td")[4].text.strip()
    # added the goal average
    goal_average_team = team.find_all("td")[11].text.strip()
    teams.append({
        "name": team_name,
        "position": team_position,
        "points": team_points,
        "played games": team_played_games,
        "goal average": goal_average_team
    })

# print(*teams, sep='\n')
# writing in a csv file
with open("football.csv", "w") as f:
    for team in teams:
        writer = csv.DictWriter(f, team.keys())
        writer.writerow(team)

# append to a csv file
# read a new team and add it to the csv file
# add information to the csv file
keys = ["name", "position", "points", "played games", "goal average"]
with open("football.csv", "a") as f:
    print("Write \"read\" if you want to read a team or \"quit\" if you want to stop reading teams")
    while 1:
        command = input()
        if command == "read":
            new_team = {}
            print("This is the information of a team", keys)
            values = [x for x in input().split(",")]
            for i in range(len(values)):
                new_team[keys[i]] = values[i]
            writer = csv.DictWriter(f, new_team.keys())
            writer.writerow(new_team)
            print("Team added to the csv file")
        elif command == "quit":
            break

# reading from a csv file
with open("football.csv", "r") as f:
    reader = csv.DictReader(f, keys)
    for row in reader:
        if row not in teams:
            teams.append(row)
print(*teams, sep="\n")

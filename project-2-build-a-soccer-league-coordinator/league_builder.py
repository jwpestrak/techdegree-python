import math
import random

players = []

with open('soccer_players.csv', mode='r') as f:
    for line in f:
        if line.startswith('Name'): # ignore header line
            next
        players.append(line.split(','))

def determine_team_size(players, teams):
    """Determine minimum count of players to be assigned to each team to ensure
    that teams are equal-sized (or close to).
    """
    player_count = len(players)
    team_count = len(teams)
    return math.floor(player_count / team_count)
    

def make_teams(players, teams):
    """Take a list of player data and a list of team names to make equal-sized 
    teams.  Each team will have the same distribution of experience.
    """

    # determine minimum team size
    min_players_per_team = determine_team_size(players, teams) 

    # split players by experience
    experience_yes = []
    experience_no = []
    for player in players:
        if player[2] == "YES":
            experience_yes.append(player)
        elif player[2] == "NO":
            experience_no.append(player)
        else:
            print(player[0], "has a null value for experience.")
    

    # assign players to teams
    my_teams = {}
    for team in teams:
        my_teams[team] = [] 

    # ensure each team has requisite count of experienced players
    experienced_players_per_team = determine_team_size(experience_yes, teams)
    for team in my_teams.keys():
        while len(my_teams[team]) < experienced_players_per_team:
           my_teams[team].append(experience_yes.pop())

    # ensure each team is of at least minimum team size
    for team in my_teams.keys():
        while len(my_teams[team]) < min_players_per_team:
           my_teams[team].append(experience_no.pop())
    while len(experience_yes) > 0:
        my_teams[random.choice(teams)].append(experience_yes.pop())

    return my_teams

final_teams = make_teams(players, ['Sharks', 'Dragons', 'Raptors'])

# output file named teams.txt with name of team and its players
with open('teams.txt', mode='w') as f:
    for key, value in final_teams.items():
        f.write(key+"\n")
        for player in value:
            del player[1] # remove height
            f.write(', '.join(player))
# 
if __name__ == "__main__":
    #final_teams = make_teams(players, teams)
    print(final_teams)

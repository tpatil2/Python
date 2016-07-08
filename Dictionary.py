import sys
import os
import random

#dictionary or map   kay and value pair

team_india={'Capton':'Dhoni',
            'Vice capton':'Virat Kohli',
            'Batsman':'Sharma',
            'Baller':'Bumra',
            'Spinner':'Jadeja'}

print('Team India Keys',team_india.keys())

print('Team India Values',team_india.values())

print('captain is',team_india['Capton'])

del team_india['Capton']

print('Team India Keys',team_india.keys())
print('Team India Values',team_india.values())

team_india['Batsman']='Rahane'

print('Team India Keys',team_india.keys())
print('Team India Values',team_india.values())

print('length is', len(team_india))

print('Vice Captain is',team_india.get("Vice capton"))

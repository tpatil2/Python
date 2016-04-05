import random
import sys
import os


pi_tuple=(2,4,6,3,2,2,57,8)

print(pi_tuple)

new_list=list(pi_tuple)

print(new_list)

print(max(pi_tuple))
print(min(pi_tuple))
print(len(pi_tuple))

#dictionary

team_india={'Capton':'Dhoni',
            'Vice capton':'Kohli',
            'Batsman':'Sharma',
            'Baller':'Bumra',
            'Spinner':'Jadeja'}

print('Team India Keys',team_india.keys())
print('Team India Values',team_india.values())

print('captain is',team_india['Capton'])

del team_india['Spinner']

print('Team India Keys',team_india.keys())
print('Team India Values',team_india.values())

team_india['Batsman']='Rahane'

print('Team India Keys',team_india.keys())
print('Team India Values',team_india.values())

print('length is', len(team_india))

print('Vice Captain is',team_india.get("Vice capton"))
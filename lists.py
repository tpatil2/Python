import random
import sys
import os



team_list = ['India', 'Pakistan', 'West Indies', 'Shrilanka']


print(team_list)
print(team_list[2])
team_list[1] = "over"
print(team_list[1:3],"\n")# print elements between given range not include index 3



Players_India=['Kohli','Dhoni','sharma','Raina','yuvraj']

print(Players_India,'\n')
print(Players_India[1])
print('\n')


comb_player=[team_list,Players_India]

print(comb_player)
print((comb_player[1][0]))  #[list number][element index]

print('append England')
team_list.append('England')
print(team_list)

print('insert pandy at 0')
Players_India.insert(0,'pandy')
print(Players_India)

print('reverse it')
Players_India.reverse()
print(Players_India)

print('sort team')
Players_India.sort()
print(Players_India)

print('remove 2nd element')
Players_India.remove('Dhoni')
print(Players_India)

new_combined=Players_India+team_list

print('new_combined list')
print(new_combined)

print(len(new_combined))
print(max(new_combined))
print(min(new_combined))

print('before delete')
print(team_list)
print('delete 3 element in list')
del (team_list[3])
print(team_list)

integer_list= ['1','2','44','0','-100','100','-999','7']
print(integer_list,'\n')
integer_list.sort()
print(integer_list)
print(max(integer_list))


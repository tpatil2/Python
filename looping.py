import os
import sys
import random

# looping

#for
for x in range(0, 10):
    print(x, ' ',end="")

print('\n')

team_list = ['India', 'Mumbai', 'West Indies', 'Shrilanka']

for y in team_list:
    print(y)



numlist=[[3,4,5],[33,44,55],[333,444,555]]

for x in range(0,3):
    for y in range(0,3):
        print(numlist[x][y])

#while

num=0

while(num!=25):
    print(num)
    num=num+1

#random number

random_num = random.randrange(1,100)
while(random_num!=15):
    print(random_num)
    random_num=random.randrange(1,100)


# print even numbers

i=0

while(i<100):
    if(i%2==0):
        print(i,' is even number')
    elif(i%1==0):
        print(i,' is not even number')
    i+=1

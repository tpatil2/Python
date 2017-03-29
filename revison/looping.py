import random
import sys
import os

for x in range(1,11):
    print(x, end=" ")

print('\n')
for x in [2,3,6,8,9]:
    print(x, end=" ")

print('\n')
list = ['a','s','d','f']

for y in list:
    print(y, end=" ")



list2 =[[0,1,2,3],[10,11,12,13],[20,21,22,23]]

for x in range(0,3):
    for y in range(0,4):
        print(list2[x][y])



random_num = random.randrange(0,20)

while(random_num != 10):
    print(random_num)
    random_num = random.randrange(0, 20)

print(random_num)
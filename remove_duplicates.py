import sys
import random
import os


#this function convert string to list
def convTolist(mystring):
    temp = []
    for i in mystring:
        temp.append(i)
    return temp


def remove_dup(mylist):
    i=1
    j=1

    while(j != len(mylist)):
        if mylist[j] != mylist[j-1]:
            mylist[i]=mylist[j]
            i+=1
        j+=1
    #convert list to string
    mystring = ''.join(mylist[0:i])
    return mystring


def prep_remove(mystring):
    mylist = convTolist(mystring)
    mylist.sort()
    return remove_dup(mylist)


mystring="hello"
print prep_remove(mystring)

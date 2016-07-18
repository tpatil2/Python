import sys
import os
import random




print('Enter your Name')

name=sys.stdin.readline()

def unique_char(str):
    if len(str) > 128: return False

    arr = [False] * 128

    for char in str:
        if arr[ord(char)] is False:
            arr[ord(char)] = True
        else:
            return False
    return True


if unique_char(name) is True:
        print "The string has unique letters"
else:
        print "The string has repeating letters"

import os
import sys
import random


test_file = open("test.txt","wb")

print(test_file.mode)
print(test_file.name)

test_file.write(bytes("Hi this is Tejas Patil\n",'UTF-8'))

test_file.close()

test_file = open("test.txt","r+")

read = test_file.read()

print(read)

os.remove("test.txt")
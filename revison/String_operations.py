import os
import sys
import random


long_str = "my name is tejas patil"

print(long_str[0:4])
print(long_str[-5:])
print(long_str[0:-2])

print(long_str[0:8]+ "is tejas")


print("my grade is %c and my GPS is %.3f and I graduated in %s"%
        ('A',3.6767,'CS'))

print(long_str.capitalize())
print(long_str.isalpha())
print(long_str.isalnum())
print(long_str.islower())
print(long_str.find("name"))
print(len(long_str))
print(long_str.replace("name", "full name"))
print(long_str.strip())

list1 = long_str.split(" ")
print(list1)
import os
import sys
import random


long_string = " i am the theme of my life     "

print(long_string.capitalize())
print(long_string.strip())
print(long_string.find('theme'))
print(long_string.isnumeric())
print(long_string.isprintable())
print(long_string.replace("i am","you are"))
print(len(long_string))


quote_list=long_string.split(" ")
print(quote_list)

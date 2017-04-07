import os
import sys
from os import path


#write file
file = open('myfile.txt','w')

file.write('this is my test fiel\n')

file.write('this is second line\n')

file.close()


#read file

fr = open('myfile.txt','r')

text = fr.read()

print(text)
fr.close()


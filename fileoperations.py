import os
import sys
import random


# wb creates new file removes old file content
# ab+ opens existing or creat new and append to ols file if exists


#write to files
test_file = open("myfile.txt","wb")

print(test_file.name)
print(test_file.mode)

test_file.write(bytes("My name is Tejas Patil\n",'UTF-8'))
test_file.close()


#read from file

test_file = open("myfile.txt","r+")

text_in_file = test_file.read()
print(text_in_file)

test_file.close()

#remove file

os.remove("myfile.txt")
os.remove("myfile2.txt")
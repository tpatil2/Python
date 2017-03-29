import subprocess


#parst to out of the commnad cat to the output

output = subprocess.getoutput('cat test.txt')

#count number of vowels in the text file

num = output.count("a")
num += output.count("e")
num += output.count("i")
num += output.count("o")
num += output.count("u")

print("Number of Vowels in the test.txt file are: ", num)


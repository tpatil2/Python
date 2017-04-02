import random

vowels = ('a','e','i','o','u')

sentance = input("Please enter your string:\n")

result = ""

for letter in sentance:
    if letter not in vowels:
        result+=letter
    else:
        temp=random.choice(vowels)
        while(temp == letter):
            temp=random.choice(vowels)
        result+=temp



print("string after removing vowels")
print(result)

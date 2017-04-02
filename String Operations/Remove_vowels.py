
vowels = ('a','e','i','o','u')

sentance = input("Please enter your string:\n")

result = ""

for letter in sentance:
    if letter not in vowels:
        result+=letter
    elif letter in vowels:
        print('This is vowels: ', letter)


print("string after removing vowels")
print(result)
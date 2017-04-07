

# does not print duplicates

groceries = {'milk','eggs','bread','rice', 'eggs'}

print(groceries)

if 'milk' in groceries:
    print("you already have")
else:
    print("you need milk")



trip = {'pune':'collge','islampur':'home','kota':'classes','chico':'MS'}


for k,v in trip.items():
    print(k,"is ",v)



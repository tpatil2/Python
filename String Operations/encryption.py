
letters = {"A":"E", "B":"F","C":"G","D":"H","E":"I","F":"J","G":"K","H":"L","I":"M","J":"N","K":"N","L":"O","M":"P","N":"Q","O":"R",
           "P":"S","Q":"T","R":"U","S":"V","T":"W","U":"X","V":"Y","W":"Z","X":"A","Y":"B","Z":"C"}


message = input("Enter the message to be encrypted:\n").upper()

encrypted=""

for letter in message:
    if letter in letters:
        encrypted+=letters[letter]
    else:
        encrypted+=letter

print('plane Text is :', message)
print('Cypher Text is: ',encrypted)


'''outout

Enter the message to be encrypted:
This is not my apple
plane Text is : THIS IS NOT MY APPLE
Cypher Text is:  WLMV MV QRW PB ESSOI

Process finished with exit code 0

'''
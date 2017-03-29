

def main():

    file = open("yesno.txt","r")
    lines = file.readlines()
    file.close()

    count_yes = 0
    count_no = 0

    for line in lines:
        line=line.strip().upper()
        if line.find("YES") != -1 and len(line)==3:
            count_yes = count_yes+1
        elif line.find("NO") != -1 and len(line)==2:
            count_no = count_no+1

    print("YES: " , count_yes)
    print("NO: ", count_no)







main()
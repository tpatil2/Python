
'''This is a sample script for tip calulater'''


def cal_tip():

    bill = float(input("Enter Total Bill Amount?\n"))
    print("How mauh percent tip you wnat to give ?")

    tip = float(input("10% , 15%, 20% Enter any value\n"))

    spl = input("If you want to split amount Yes/No?\n")

    if spl == 'Yes' or spl == 'yes':
        split = float(input("how Many People?\n"))

    total_bill = bill + (bill/100)*tip
    indv_bill = total_bill/split

    print("==================================")
    print("Original Bill is : ", bill)
    print("tip  ampunt is : ", (bill/100)*tip)
    print("==================================")
    print("Total Bill is : ", total_bill)
    print("Individual Bill is", indv_bill)


cal_tip()
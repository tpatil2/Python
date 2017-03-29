import sys
import os
import random


# Provide menu option to user
# function for currency conerter




def curr_conver():
    choice = ""
    while(choice != "Q"):
        print("Please enter you Choice")
        print(" 1) USD to INR","\n","2) INR to USD")
        print("Press Q to Exit")
        choice = input("Choice ? ")
        print(choice)
        print("-------------------------------------")
        if choice == "1":
            print("USD to INR")
            USD_amt = float(input("ENTER AMOUT IN USD "))
            print("Amount after conversition is: " )
            INR_amt = USD_amt*64.93
            print("Amont after Conversion", "$",USD_amt,"= %.2f"%INR_amt ,"Ruppes")
            print("-------------------------------------")


        elif choice == "2":
            print("INR to USD")
            INR_amt = float(input("ENTER AMOUT IN INR "))
            print("Amount after conversition is: ")
            USD_amt = INR_amt * 0.015
            print("Amont after Conversion", "Ruppes", INR_amt, "= $ %.3f" %USD_amt)
            print("-------------------------------------")


        else:
            print("Please enter correct choice")


curr_conver()

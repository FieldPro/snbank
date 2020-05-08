import csv
import string
import random
import os
import sys
import math

#users = {}
login = ""
options = ""
accountName = ""
openingBal = ""
accountType = ""
accountName = ""
accNumOrigin = ""
accNumOri = ""
contents1 = ""

def displayMenu():
    options = input("If you want to login. Enter yes or enter quit to close app: ")

    if options == "yes":
        oldUser()
    elif options == "quit":
        #displayMenu()
        sys.exit()

def oldUser():
    login = input('Enter username: ')
    passw = input('Enter password: ')
    file = open("staff.txt", "r")
    for row in file:
        field = row.split(",")
        username = field[0]
        password = field[1]

        if login == username and passw == password:
            print("\nLogin successful!\n")
            session()
            staffTask()
            #break
        else:
            print("User does not exist or wrong password!")

def staffTask():
    sTask = input("Enter A to create new bank account. Enter B to check account details. C to Logout: ")

    if sTask == "A":
        nbte()
    elif sTask == "B":
        accDetails()
    else:
        logOut()

def nbte():
    accountName = input("Enter Account Name: ")
    openingBal = input("Enter Opening Balance: ")
    accountType = input("Enter Account Type: ")
    accountEmail = input("Enter Account Email: ")
    accNumOri = ''.join(random.choice(string.digits) for _ in range(10))
    print(accNumOri)
    details = accountName + "," + "$" + openingBal + "," + accountType + "," + accountEmail + "," + accNumOri
    f = open("customer.txt", "w")
    for i in range(1):
        f.write(details)
    f.close()
    staffTask()

def accDetails():
    accNum = input("Enter customer's account number: ")
    file = open("customer.txt")
    for row in file:
        field = row.split(",")
        accNo = field[4]

        if accNum == accNo:
            print(row)
            file.close()
            staffTask()
        else:
            displayMenu()

def logOut():
    os.remove("userSession.txt")
    displayMenu()

def session():
    f = open("userSession.txt", "w")
    for i in range(1):
        f.write("user logged in!")
    f.close()

while options != "quit":
    displayMenu()
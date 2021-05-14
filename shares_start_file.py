import shares_navigation_file as menus
import shares_invest_file as shares
import shares_cash_file as cashAccount
import database as db


import os
from art import *
import pyfiglet
from pyfiglet import figlet_format
import time
from threading import Thread


def clearScreen():
    os.system('cls')


# INITIALISES PROJECT
def startUp():
    """ This function initialises the program and creates a database """
    db.createTable_Customers()
    db.insert_initailDataSet()
    print(pyfiglet.figlet_format("Jacob Horgan Python Presentation"))
    tprint("ONLINE", font="block", chr_ignore=True)
    tprint("\nSHARES", font="block", chr_ignore=True)
    print(menus.startMenu)
    print(menus.startMenuSwitch(input("Please enter your menu selection: ")))
    if menus.loginMenuActive:
        menus.loginScreen()
    elif menus.registerMenuActive:
        menus.registerScreen()


# UPDATES USER INFO ON THE SCREEN
def updateScreenAccountInfo():
    """ This function updates the information displayed on the screen. Account value etc. """
    shares.calculateTotalInvestAccount()
    print("Hello", menus.loggedUser[0][0] +
          "! Welcome to your online shares trading account.\n")

    print("\nShare Prices:")
    print("Share 1 price per share: ".ljust(
        25, ' '), "£", shares.share1rounded)
    print("Share 2 price per share: ".ljust(
        25, ' '), "£", shares.share2rounded)
    print("Share 3 price per share: ".ljust(
        25, ' '), "£", shares.share3rounded)
    print("\nYour Assets:")
    print("Cash Account Value: ".ljust(25, ' '), "£",
          format(cashAccount.cashAccount, ".2f"))
    print("Investing Account Value: ".ljust(25, ' '), "£",
          format(shares.investAccount, ".2f"))
    print("\n")


# LOOPS THROUGH THE MAIN MENU
def menuLoop():
    """ This function loops through the main menu checking for an input """
    if menus.mainMenuActive:
        print(menus.menuPicture)
        updateScreenAccountInfo()
        print(menus.mainMenuSwitch(input("Please enter your menu selection: ")))
    elif menus.depositMenuActive:
        updateScreenAccountInfo()
        print(menus.depositMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.withdrawMenuActive:
        updateScreenAccountInfo()
        print(menus.withdrawMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.investMenuActive:
        updateScreenAccountInfo()
        print(menus.investMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.sharesMenuActive:
        updateScreenAccountInfo()
        print(menus.sharesMenuSwitch(
            input("Please enter your menu selection: ")))
    elif menus.accountMenuActive:
        updateScreenAccountInfo()
        print(menus.accountMenuSwitch(
            input("Please enter your menu selection: ")))


def mainLoop():
    menuLoop()
    shares.updateAllShares()


startUp()
while 1:
    mainLoop()

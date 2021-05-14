import os
import shares_cash_file as cashAccount
import shares_invest_file as shares
import time
import database


mainMenuList = ("1", "2", "3", "4", "5", "X", "x", "R", "r")
cashMenuList = ("1", "X", "x")
investMenuList = ("1", "2", "3", "X", "x")
sharesMenuList = ("1", "2", "3", "X", "x")
accountMenuList = ("1", "2", "3", "X", "x")
startMenuList = ("1", "2")


startMenuActive = True
loginMenuActive = False
registerMenuActive = False
mainMenuActive = False
subMenuActive = False
depositMenuActive = False
withdrawMenuActive = False
investMenuActive = False
sharesMenuActive = False
accountMenuActive = False

loggedUser = []


def clearScreen():
    os.system('cls')


# START UP MENU
def startMenuSwitch(selection):
    """ This function displays the Welcome menu and asks if user wants to login or register """
    global loginMenuActive
    global registerMenuActive
    global startMenuActive
    if selection in startMenuList:
        if selection == "1":
            loginMenuActive = True
            startMenuActive = False
            clearScreen()
            return login
        elif selection == "2":
            registerMenuActive = True
            startMenuActive = False
            clearScreen()
            return register
    else:
        print("Please enter a valid input")
        startMenuSwitch(input("Please enter your menu selection: "))


# LOGIN MENU
def loginScreen():
    """ This function displays the Login screen and asks the user to enter their name and password """
    global loginMenuActive
    global mainMenuActive
    global loggedUser
    userName = getName()
    password = getPassword()
    loggedUser = database.fetchAccountName(userName)
    if loggedUser == []:
        print("That username does not exist. Please try again.")
        time.sleep(1)
        clearScreen()
        print(login)
        loginScreen()
    elif loggedUser[0][1] == password:
        print("Welcome back ", userName)
        time.sleep(1)
        getCashAccount()
        getInvestAccount()
        clearScreen()
        mainMenuActive = True
        loginMenuActive = False
    elif loggedUser[0][1] != password:
        print("Incorrect Password. Please try again.")
        time.sleep(1)
        clearScreen()
        print(login)
        loginScreen()


# REGISTER SCREEN
def registerScreen():
    """ This function displays the register screen and asks the user to input a name and password """
    global loginMenuActive
    global registerMenuActive
    userName = getName()
    password = getPassword()
    database.createNewAccount(userName, password, 0, 0)
    time.sleep(1)
    clearScreen()
    print(login)
    loginMenuActive = True
    registerMenuActive = False
    loginScreen()


# ASKS FOR NAME
def getName():
    """ This function asks the user to input their name and returns it capitilsed and as one variable """
    firstName = input("Please type your first name: ")
    secondName = input("Please type your second name: ")
    firstNameCap = firstName.capitalize()
    secondNameCap = secondName.capitalize()
    fullName = (firstNameCap + " " + secondNameCap)
    return fullName


# ASKS FOR PASSWORD
def getPassword():
    """ This function asks the user to enter a password and returns it """
    password = input("Please type your password: ")
    return password


# GETS CASH ACCOUNT FROM DATABASE
def getCashAccount():
    """ This function gets cash account value from database """
    global loggedUser
    cashAccount.cashAccount = loggedUser[0][2]


# GETS INVEST ACCOUNT FROM DATABASE
def getInvestAccount():
    """ This function gets invest account value from database """
    global loggedUser
    shares.investAccount = loggedUser[0][3]


# MAIN MENU
def mainMenuSwitch(selection):
    """ This function checks for user input on the main menu """
    shares.updateAllShares()
    global mainMenuActive
    global subMenuActive
    global depositMenuActive
    global withdrawMenuActive
    global investMenuActive
    global sharesMenuActive
    global accountMenuActive
    if selection in mainMenuList:
        if selection == "1":
            depositMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem1
        elif selection == "2":
            withdrawMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem2
        elif selection == "3":
            investMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem3
        elif selection == "4":
            sharesMenuActive = True
            mainMenuActive = False
            clearScreen()
            return print(menuItem4.format(shares.share1, shares.share2, shares.share3))
        elif selection == "5":
            accountMenuActive = True
            mainMenuActive = False
            clearScreen()
            return menuItem5
        elif selection == "R" or selection == "r":
            clearScreen()
    else:
        print("Please enter a valid input")
        mainMenuSwitch(input("Please enter your menu selection: "))


# SUB MENU TEMPLATE
def subMenuSwitch(selection):
    """ This function checks for user input on the sub menu 'template menu' """
    shares.updateAllShares()
    global mainMenuActive
    global subMenuActive
    if selection in mainMenuList:
        if selection == "1":
            clearScreen()
            return "Item coming soon"
        elif selection == "2":
            clearScreen()
            return "Item coming soon"
        elif selection == "3":
            clearScreen()
            return "Item coming soon"
        elif selection == "4":
            clearScreen()
            return "Item coming soon"
        elif selection == "X" or selection == "x":
            clearScreen()
            subMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        subMenuSwitch(input("Please enter your menu selection: "))


# DEPOSIT MENU
def depositMenuSwitch(selection):
    """ This function checks for user input on the deposit menu """
    shares.updateAllShares()
    global mainMenuActive
    global depositMenuActive
    if selection in cashMenuList:
        if selection == "1":
            cashAccount.depositScreen()
            time.sleep(2)
            clearScreen()
            depositMenuActive = False
            mainMenuActive = True
        elif selection == "X" or selection == "x":
            clearScreen()
            depositMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        depositMenuSwitch(input("Please enter your menu selection: "))


# WITHDRAW MENU
def withdrawMenuSwitch(selection):
    """ This function checks for user input on the withdraw menu """
    shares.updateAllShares()
    global mainMenuActive
    global withdrawMenuActive
    if selection in cashMenuList:
        if selection == "1":
            cashAccount.withdrawScreen()
            time.sleep(2)
            clearScreen()
            withdrawMenuActive = False
            mainMenuActive = True
        elif selection == "X" or selection == "x":
            clearScreen()
            withdrawMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        withdrawMenuSwitch(input("Please enter your menu selection: "))


# INVEST MENU
def investMenuSwitch(selection):
    """ This function checks for user input on the invest menu """
    shares.updateAllShares()
    global mainMenuActive
    global investMenuActive
    if selection in investMenuList:
        if selection == "1":
            shares.buySharesScreen()
            time.sleep(2)
            clearScreen()
            investMenuActive = False
            mainMenuActive = True
        elif selection == "2":
            shares.sellSharesScreen()
            time.sleep(2)
            clearScreen()
            investMenuActive = False
            mainMenuActive = True
        elif selection == "3":
            shares.viewPortfolioScreen()
            time.sleep(2)
            clearScreen()
            investMenuActive = False
            mainMenuActive = True
        elif selection == "X" or selection == "x":
            clearScreen()
            investMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        sharesMenuSwitch(input("Please enter your menu selection: "))


# SHARES INFO MENU
def sharesMenuSwitch(selection):
    """ This function checks for user input on the shares menu """
    shares.updateAllShares()
    global mainMenuActive
    global sharesMenuActive
    if selection in sharesMenuList:
        if selection == "1":
            shares.displayShare1()
            clearScreen()
            mainMenuSwitch("4")
        elif selection == "2":
            shares.displayShare2()
            clearScreen()
            mainMenuSwitch("4")
        elif selection == "3":
            shares.displayShare3()
            clearScreen()
            mainMenuSwitch("4")
        elif selection == "X" or selection == "x":
            clearScreen()
            sharesMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        sharesMenuSwitch(input("Please enter your menu selection: "))


# ACCOUNT INFO MENU
def accountMenuSwitch(selection):
    """ This function checks for user input on the account menu """
    shares.updateAllShares()
    global mainMenuActive
    global loginMenuActive
    global accountMenuActive
    global loggedUser
    if selection in accountMenuList:
        if selection == "1":
            setNewName()
            time.sleep(2)
            clearScreen()
            accountMenuActive = False
            mainMenuActive = True
        elif selection == "2":
            setNewPassword()
            time.sleep(2)
            clearScreen()
            accountMenuActive = False
            mainMenuActive = True
        elif selection == "3":
            logoutUser()
            print("Logging out...")
            time.sleep(2)
            clearScreen()
            print(login)
            loginMenuActive = True
            loginScreen()
        elif selection == "X" or selection == "x":
            clearScreen()
            accountMenuActive = False
            mainMenuActive = True
            return " "
    else:
        print("Please enter a valid input")
        sharesMenuSwitch(input("Please enter your menu selection: "))


# SETS A NEW USERNAME
def setNewName():
    """ This function updates the users username on database """
    global loggedUser
    print("This will update your username on our database.")
    newName = getName()
    database.updateAccountName(loggedUser[0][0], newName)
    loggedUser = database.fetchAccountName(newName)


# SETS A NEW PASSWORD
def setNewPassword():
    """ This function updates the users password on database """
    global loggedUser
    print("This will update your password on our database.")
    newPassword = getPassword()
    database.updateAccountPassword(loggedUser[0][1], newPassword)
    loggedUser = database.fetchAccountName(loggedUser[0][0])


# LOGS USER OUT
def logoutUser():
    """ This function logs the user out and updates cash and ivest account values on database """
    global loggedUser
    global loginMenuActive
    newCash = cashAccount.cashAccount
    print(newCash)
    print(loggedUser[0][0])
    database.updateAccountCash(
        loggedUser[0][0], newCash)


# START MENU
startMenu = """

                                        #############################################
                                        #               WELCOME                     #
                                        #                                           #
                                        #       1 -     Login                       #
                                        #       2 -     Register                    #
                                        #                                           #
                                        #                                           #
                                        #                                           #  
                                        #                                           #
                                        #############################################

"""

# LOGIN MENU
login = """

                                        #############################################
                                        #               LOGIN SCREEN                #
                                        #                                           #
                                        #       Please enter your username          #
                                        #       and password to continue.           #
                                        #                                           #
                                        #                                           #
                                        #       X -     Back to Welcome Screen      #  
                                        #                                           #
                                        #############################################

"""

# REGISTER MENU
register = """

                                        #############################################
                                        #               REGISTER SCREEN             #
                                        #                                           #
                                        #       Please create a username            #
                                        #       and password to continue.           #
                                        #                                           #
                                        #                                           #
                                        #       X -     Back to Welcome Screen      #  
                                        #                                           #
                                        #############################################

"""

# MAIN MENU
menuPicture = """

                                        #############################################
                                        #               MAIN MENU                   #
                                        #                                           #
                                        #       1 -     Cash Deposit                #
                                        #       2 -     Cash Withdraw               #
                                        #       3 -     Invest Account              #
                                        #       4 -     Shares Info                 #
                                        #       5 -     Account Info                #
                                        #                                           #
                                        #############################################

"""

# DEPOSIT MENU
menuItem1 = """


                                        #############################################
                                        #               CASH DEPOSIT                #             
                                        #                                           #
                                        #       Deposits will be rounded to 1       #
                                        #       decimal point. Limit of £500.       #
                                        #                                           #
                                        #       1 -     Proceed                     #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

# WITHDRAW MENU
menuItem2 = """


                                        #############################################
                                        #               CASH WITHDRAW               #             
                                        #                                           #
                                        #       No limit, but you can't             #
                                        #       withdraw money you don't have.      #
                                        #                                           #
                                        #       1 -     Proceed                     #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

# INVEST MENU
menuItem3 = """


                                        #############################################
                                        #               INVEST ACCOUNT              #             
                                        #                                           #
                                        #       1 -     Buy Shares                  #
                                        #       2 -     Sell Shares                 #
                                        #       3 -     View Portfolio              #
                                        #       4 -                                 #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

# SHARES INFO MENU
menuItem4 = """


                                        #############################################
                                        #               SHARES INFO                 #             
                                        #                                           #
                                        #       1 -     Share 1 = {0:.1f}               #
                                        #       2 -     Share 2 = {1:.1f}               #
                                        #       3 -     Share 3 = {2:.1f}               #
                                        #                                           #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

# ACCOUNT INFO MENU
menuItem5 = """


                                        #############################################
                                        #               ACCOUNT INFO                #             
                                        #                                           #
                                        #       1 -     Update username             #
                                        #       2 -     Update password             #
                                        #       3 -     Logout                      #
                                        #                                           #
                                        #       X -     Back to Main Menu           #
                                        #                                           #
                                        #############################################

"""

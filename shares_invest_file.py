import random
import time
import schedule
import shares_cash_file as cashAccount


shareMenuList = ("1", "2", "3")

investAccount = float(0.0)

share1 = float(1.0)
share2 = float(1.0)
share3 = float(1.0)

share1rounded = float(1.0)
share2rounded = float(1.0)
share3rounded = float(1.0)

share1List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
share2List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
share3List = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

share1Amount = 0
share2Amount = 0
share3Amount = 0

share1investValue = 0
share2investValue = 0
share3investValue = 0


# WHAT I WOULD DO DIFFERENTLY WITH MORE TIME!
"""
shares = {1: {'value': '0.0', 'roundedValue': '0.0', 'amount': '0', 'investValue': '0'},
          2: {'value': '0.0', 'roundedValue': '0.0', 'amount': '0', 'investValue': '0'}
          3: {'value': '0.0', 'roundedValue': '0.0', 'amount': '0', 'investValue': '0'}}
"""


# SHIFT LIST TO THE LEFT
def shiftLeft(sequence, shiftNum=0):
    """ This function shifts values in a list to left by n times """
    shiftValue = shiftNum % len(sequence)
    return sequence[+shiftValue:] + sequence[:+shiftValue]


# SHIFT ALL SHARES
def shareShift():
    """ This function shifts all shares """
    global share1List
    global share2List
    global share3List

    share1List = shiftLeft(share1List, 1)
    share1List[-1] = share1rounded

    share2List = shiftLeft(share2List, 1)
    share2List[-1] = share2rounded

    share3List = shiftLeft(share3List, 1)
    share3List[-1] = share3rounded


# UPDATE SHARES EVERY SECOND WITH RANDOM VALUES
def updateShares():
    """ This function updates all shares with random values between 0.1 - 0.8 either up or down every second """
    global share1
    global share2
    global share3
    global share1rounded
    global share2rounded
    global share3rounded
    if random.random() > 0.35:
        share1 = share1 + random.uniform(0.1, 0.6)
    else:
        share1 = share1 - random.uniform(0.1, 0.6)

    if random.random() > 0.45:
        share2 = share1 + random.uniform(0.1, 0.7)
    else:
        share2 = share1 - random.uniform(0.1, 0.7)

    if random.random() > 0.4:
        share3 = share3 + random.uniform(0.1, 0.8)
    else:
        share3 = share3 - random.uniform(0.1, 0.8)

    share1rounded = round(share1, 1)
    share2rounded = round(share2, 1)
    share3rounded = round(share3, 1)

    if share1rounded <= 0:
        share1rounded = 0.1
    if share2rounded <= 0:
        share2rounded = 0.1
    if share3rounded <= 0:
        share3rounded = 0.1
    shareShift()


schedule.every(1).seconds.do(updateShares)


# CHECK USER INPUT IS NUMBER
def checkUserInput(input):
    """ This function checks to ensure the user has entered a number """
    try:
        val = float(input)
        return True
    except ValueError:
        print("\nERROR!!! Please enter a number. !!!ERROR.")
        return False


# UPDATE ALL SHARES
def updateAllShares():
    """ This function calls the schedule of 1 second """
    schedule.run_pending()


# CALCULATE SINGLE SHARE VALUE
def calculateShareValue(sharePrice, shareAmount):
    shareValue = sharePrice * shareAmount
    return shareValue


# CALCULATE TOTAL INVEST VALUE
def calculateTotalInvestAccount():
    """ This function calculates the total value of the Invest account """
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount
    global investAccount
    global share1rounded
    global share2rounded
    global share3rounded
    global share1investValue
    global share2investValue
    global share3investValue

    share1investValue = calculateShareValue(share1rounded, share1Amount)
    share2investValue = calculateShareValue(share2rounded, share2Amount)
    share3investValue = calculateShareValue(share3rounded, share3Amount)

    investAccount = share1investValue + share2investValue + share3investValue


# VIEW INVESTING PORTFOLIO INFORMATION
def viewPortfolioScreen():
    """ This function displays the portfolio screen and relevant data about share holdings """
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount
    calculateTotalInvestAccount()

    print("\nTotal Investing account is worth: £", investAccount)

    print("\nShare 1 amount of owned shares: ",
          share1Amount, "Worth: ", format(share1investValue, ".2f"))
    print("\nShare 2 amount of owned shares: ",
          share2Amount, "Worth: ", format(share2investValue, ".2f"))
    print("\nShare 3 amount of owned shares: ",
          share3Amount, "Worth: ", format(share3investValue, ".2f"))

    input("\nPress any key to return to Main Menu")


# LIVE FEED SHARE 1
def displayShare1():
    """ This function displays a live feed of Share 1 data being updated """
    global share1List
    count = 0
    print("\nViewing live prices of Share 1 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        print(share1List, end="\r")
        count += 1
        time.sleep(1)


# LIVE FEED SHARE 2
def displayShare2():
    """ This function displays a live feed of Share 2 data being updated """
    global share2List
    count = 0
    print("\nViewing live prices of Share 2 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        print(share2List, end="\r")
        count += 1
        time.sleep(1)


# LIVE FEED SHARE 3
def displayShare3():
    """ This function displays a live feed of Share 3 data being updated """
    global share3List
    count = 0
    print("\nViewing live prices of Share 3 for 5 seconds:\n")
    while count < 6:
        updateAllShares()
        print(share3List, end="\r")
        count += 1
        time.sleep(1)


# ASKS USER WHICH SHARE THEY WANT TO BUY
def buySharesScreen():
    """ This function displays the buy shares screen and asks user which share """
    updateAllShares()
    print("\nEnter which Share you would like to purchase or X to exit: ")
    shareNum = input("Share = ")
    if checkUserInput(shareNum):
        buySharesInfo(shareNum)
    else:
        buySharesScreen()


# ASKS USER HOW MUCH THEY WANT TO BUY
def buySharesInfo(shareNum):
    """ This function asks user how much cash value of a share to buy """
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount

    if shareNum in shareMenuList:
        if shareNum == "1":
            price = share1rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            if checkUserInput(value):
                share1Amount = share1Amount + \
                    buyShares(float(value), price)
            else:
                buySharesInfo(shareNum)
        elif shareNum == "2":
            price = share2rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            if checkUserInput(value):
                share2Amount = share2Amount + \
                    buyShares(float(value), price)
            else:
                buySharesInfo(shareNum)
        elif shareNum == "3":
            price = share3rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nEnter the cash amount you want to invest: ")
            value = input("Amount = ")
            if checkUserInput(value):
                share3Amount = share3Amount + \
                    buyShares(float(value), price)
            else:
                buySharesInfo(shareNum)
        elif shareNum == "X" or shareNum == "x":
            print("exit")
        else:
            print("Please enter a valid input")
            buySharesScreen()


# CALCULATES HOW MANY SHARES USER WILL GET
def buyShares(value, price):
    """ This function calculates how many shares the user will get for their buy order """
    if value <= cashAccount.cashAccount and value > 0:
        cashAccount.cashAccount = cashAccount.cashAccount - value
        shares = value/price
        sharesRounded = round(shares, 1)
        print("\nSUCCESS: You have purchased ", sharesRounded, " shares for £", value,
              ". \nReturning to the Main Menu please wait.")
    elif value > cashAccount.cashAccount:
        print("\nERROR!!! You don't have enough funds in you Cash Account. !!!ERROR. \nReturning to the Main Menu please wait.")
        sharesRounded = 0
    elif value <= 0:
        print("\nERROR!!! Please enter a value larger that 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        sharesRounded = 0
    return sharesRounded


# ASKS USER WHICH SHARE THEY WANT TO SELL
def sellSharesScreen():
    """ This function displays the sell shares screen and asks user which share """
    updateAllShares()
    print("\nEnter which Share you would like to sell or X to exit: ")
    shareNum = input("Share = ")
    sellSharesInfo(shareNum)


# ASKS USER HOW MUCH THEY WANT TO SELL
def sellSharesInfo(shareNum):
    """ This function asks user how much cash value of a share to sell """
    updateAllShares()
    global share1Amount
    global share2Amount
    global share3Amount

    if shareNum in shareMenuList:

        if shareNum == "1":
            price = share1rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nShare 1 amount of owned shares: ",
                  share1Amount, "Worth: ", share1investValue)
            print("\nEnter the cash amount you want to sell: ")
            value = input("Amount = ")
            share1Amount = share1Amount - \
                sellShares(float(value), price, shareNum)

        elif shareNum == "2":
            price = share2rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nShare 2 amount of owned shares: ",
                  share2Amount, "Worth: ", share2investValue)
            print("\nEnter the cash amount you want to sell: ")
            value = input("Amount = ")
            share2Amount = share2Amount - \
                sellShares(float(value), price, shareNum)

        elif shareNum == "3":
            price = share3rounded
            print("Share ", shareNum, " price locked at: ", price)
            print("\nShare 3 amount of owned shares: ",
                  share3Amount, "Worth: ", share3investValue)
            print("\nEnter the cash amount you want to sell: ")
            value = input("Amount = ")
            share3Amount = share3Amount - \
                sellShares(float(value), price, shareNum)

        elif shareNum == "X" or shareNum == "x":
            print("exit")
        else:
            print("Please enter a valid input")
            sellSharesScreen()


# CALCULATES HOW MANY SHARES USER WILL SELL
def sellShares(value, price, shareNum):
    """ This function calculates how many shares the user will sell for their sell order """
    if shareNum == "1":
        if value <= share1investValue and value > 0:
            cashAccount.cashAccount = cashAccount.cashAccount + value
            shares = value/price
            sharesRounded = round(shares, 1)
            print("\nSUCCESS: You have sold ", sharesRounded, " shares for £", value,
                  ". \nReturning to the Main Menu please wait.")
        elif value > share1investValue:
            print("\nERROR!!! You don't have enough shares to sell for this amount. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
        elif value <= 0:
            print("\nERROR!!! Please enter a value larger that 0. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
    elif shareNum == "2":
        if value <= share2investValue and value > 0:
            cashAccount.cashAccount = cashAccount.cashAccount + value
            shares = value/price
            sharesRounded = round(shares, 1)
            print("\nSUCCESS: You have sold ", sharesRounded, " shares for £", value,
                  ". \nReturning to the Main Menu please wait.")
        elif value > share1investValue:
            print("\nERROR!!! You don't have enough shares to sell for this amount. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
        elif value <= 0:
            print("\nERROR!!! Please enter a value larger that 0. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
    elif shareNum == "3":
        if value <= share3investValue and value > 0:
            cashAccount.cashAccount = cashAccount.cashAccount + value
            shares = value/price
            sharesRounded = round(shares, 1)
            print("\nSUCCESS: You have sold ", sharesRounded, " shares for £", value,
                  ". \nReturning to the Main Menu please wait.")
        elif value > share1investValue:
            print("\nERROR!!! You don't have enough shares to sell for this amount. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
        elif value <= 0:
            print("\nERROR!!! Please enter a value larger that 0. !!!ERROR. \nReturning to the Main Menu please wait.")
            sharesRounded = 0
    return sharesRounded

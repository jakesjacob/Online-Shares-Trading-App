cashAccount = float(0.0)


# DEPOSITS CASH AND CHECKS FOR ERRORS
def depositCash(value, cashAccount):
    """ This function deposits cash into users cash account """
    if value <= 500.0 and value > 0:
        newCashAccount = cashAccount + value
        print("\nSUCCESS: You have deposited £" + str(value) +
              ". \nReturning to the Main Menu please wait.")
    elif value > 500.0:
        print("\nERROR!!! The deposit limit is £500. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value == 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value < 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    return newCashAccount


# WITHDRAWS CASH AND CHECKS FOR ERRORS
def withdrawCash(value, cashAccount):
    """ This function withdraws cash from users cash account """
    if value <= cashAccount and value > 0:
        newCashAccount = cashAccount - value
        print("\nSUCCESS: You have withdrawn £" + str(value) +
              ". \nReturning to the Main Menu please wait.")
    elif value > cashAccount:
        print("\nERROR!!! You don't have enough funds for that. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value == 0:
        print("\nERROR!!! please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    elif value < 0:
        print("\nERROR!!! Please enter a value larger than 0. !!!ERROR. \nReturning to the Main Menu please wait.")
        newCashAccount = cashAccount
    return newCashAccount


# ASKS USER HOW MUCH THEY WANT TO DEPOSIT
def depositScreen():
    """ This function asks the user how much cash they want to deposit """
    global cashAccount
    print("\nEnter the amount you want to deposit: ")
    value = input("Amount = ")
    if checkUserInput(value) == True:
        cashAccount = depositCash(float(value), cashAccount)
    else:
        depositScreen()


# ASKS USER HOW MUCH THEY WANT TO WITHDRAW
def withdrawScreen():
    """ This function asks the user how much cash they want to withdraw """
    global cashAccount
    print("\nEnter the amount you want to withdraw: ")
    value = input("Amount = ")
    if checkUserInput(value) == True:
        cashAccount = withdrawCash(float(value), cashAccount)
    else:
        withdrawScreen()


# CHECKS USER INPUT IS NUMBER
def checkUserInput(input):
    try:
        # Convert it into float
        val = float(input)
        return True
    except ValueError:
        print("\nERROR!!! Please enter a number. !!!ERROR.")
        return False

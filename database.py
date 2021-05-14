import sqlite3
from _sqlite3 import OperationalError

"""
table is entity
column = attritube
row = instance
"""


def createTable_Customers():
    """createTable_Customers will create the database table(s)"""
    connection = sqlite3.connect("online_shares.db")
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS customers')
    cursor.execute(
        "CREATE TABLE customers (custName TEXT, custPassword  TEXT, custCash FLOAT, custInvest FLOAT)")
    connection.close()


def insert_initailDataSet():
    """insert_initailDataSet will add initial data to the database table(s)"""
    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        starter_accounts = [
            ("John Hank", "password", 100, 0),
            ("Amy", "password2", 50, 0),
            ("Matt", "password3", 305, 0),
            ("Claire", "password4", 0, 0)
        ]

        cursor.executemany(

            'INSERT INTO customers VALUES (?,?,?,?)', starter_accounts)
        connection.commit()
        print("Bulk rows added successfully")

    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT many records at a time")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def createNewAccount(custName, custPassword, custCash, custInvest):
    """createNewAccount will add specified data to the database table(s)"""
    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO customers (custName, custPassword, custCash, custInvest)  VALUES (? , ? , ? , ?)",
                       (custName, custPassword, custCash, custInvest))
        connection.commit()
        print("one record added successfully")
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def fetchAccountName(findThis_name):
    """fetchAccount_By_Name will fetch/select matching data for the specified name"""
    rowSet = ()

    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()
        rowSet = cursor.execute(
            "SELECT custName, custPassword, custCash, custInvest FROM customers WHERE custName = ?",
            (findThis_name,),
        ).fetchall()
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on Fetch")
        connection.rollback()
    finally:
        connection.close()
        return rowSet


def updateAccountName(currentName,  newName):
    """UpdateAccount_Detail will Update customer name for the given ID"""

    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE customers SET  custName   = :who  WHERE custName = :whoseID",
            {"who": newName, "whoseID": currentName}
        )
        connection.commit()
        print("Account_Detail for:",  currentName,
              " Updated successfully to:", newName)

    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def updateAccountPassword(currentPassword,  newPassword):
    """UpdateAccount_Detail will Update customer name for the given ID"""

    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE customers SET  custPassword   = :who  WHERE custPassword = :whoseID",
            {"who": newPassword, "whoseID": currentPassword}
        )
        connection.commit()
        print("Account_Detail for:",  currentPassword,
              " Updated successfully to:", newPassword)

    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def updateAccountCash(userName, newCash):
    """UpdateAccount_Detail will Update customer name for the given ID"""

    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE customers SET  custCash = ?  WHERE custName = ?",
            (newCash, userName)
        )
        print("success")
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()


def updateAccountInvest(userName, newInvest):
    """UpdateAccount_Detail will Update customer name for the given ID"""

    try:
        connection = sqlite3.connect("online_shares.db")
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE customers SET  custInvest = ?  WHERE custName = ?",
            (newInvest, userName)
        )
        print("success")
    except OperationalError as errMsg:
        print(errMsg)
    except:
        print("error on INSERT")
        connection.rollback()
    else:
        print("Success, no error!")
    finally:
        connection.close()

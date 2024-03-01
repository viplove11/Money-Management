import os
import time
import mysql.connector as connector
from datetime import datetime


connectionObject = connector.connect(host = "localhost", user = "root", password ="root", database ="Budget")
cursorObject = connectionObject.cursor()


def registration(name , password):
    query = "insert into admin(admin_name,admin_pass)values('{}','{}')".format(name,password)
    cursorObject.execute(query)
    connectionObject.commit()
    
    query = "select admin_id from admin where admin_name = '{}' and admin_pass ='{}'".format(name,password)
    cursorObject.execute(query)
    adminId = cursorObject.fetchone()
    
    if adminId:
        print("Generated admin id is : '{}'".format(adminId))
        return True
    else:
        return False

def isLogged(adminId, name, password):
    query = " select admin_name, admin_pass from admin where admin_id = {}".format(adminId)
    cursorObject.execute(query)
    
    Data = cursorObject.fetchone()
    if Data[0] == name:
        if Data[1] == password:
            return True
        else:
            print("Incorrect Password")
    else:
        print("Incorrect Username")
    
    return False

def deposit(dAmount):
    current_time = datetime.now()
    query = "insert into deposit(Date_time,deposit_amount) value('{}',{})".format(current_time, dAmount)
    cursorObject.execute(query)
    connectionObject.commit()
    return True

    
    
    
    
option = "y"
while option == "y":
    print("Budget Management")
    print("1.Registration.\n2.Login")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        print("registration form")
        adminName = input("Enter the Admin name: ") 
        adminPass = input("Enter the Admin Password: ")
        if registration(name = adminName, password = adminPass):
            print("Registered Succesfully")
        else:
            print("Not registered successfully")
            
    elif choice == 2:
        id = input("Enter admin ID: ")
        userName = input("Enter admin Name: ")
        password = input("Enter admin password: ")
        
        if isLogged(adminId = id, name = userName, password = password):
            print("Succeesfull logged in")
            WantAgain = "y"
            while WantAgain == "y":
                os.system("cls")
                print("1.Deposit\n2.Withdraw.\n3.Transaction Display.\n4.Budget Display.")
                FunctionOption = int(input("Choose the option: "))
                if FunctionOption == 1:
                    os.system("cls")
                    print("Deposit Amount")
                    DepositAmount = float(input("Enter the amount to be deposited: "))
                    if deposit(DepositAmount):
                        print("Amount is Deposited")
                    else:
                        print("Amount is not Deposited")             
                elif FunctionOption == 2:
                    os.system("cls")
                    query = "select sum(deposit_amount) from deposit"
                    cursorObject.execute(query)

                    depAmt = cursorObject.fetchone()[0]
                    # print(depAmt)
                    withdrawAmount = float(input("Enter the amount to withdraw: "))
                    category=""
                    reason=""
                    
                    if withdrawAmount < depAmt:
                        depAmt = depAmt - withdrawAmount
                        print("'H' for Home Expense.")
                        print("'P' for Personal Expense.")
                        print("'F' for Fuel Expense.")
                        print("'D' for Debt.")
                        categoryOption = input("Enter Category : ")
                        if categoryOption == "H":
                            category = "Home"
                        elif categoryOption == "P":
                            category ="Personal" 
                        elif categoryOption == "F":
                            category ="Fuel" 
                        elif categoryOption == "D":
                            category ="Debt"
                        current = datetime.now()
                        reason = input("Enter reason: ")
                        query = "insert into withdraw(date_time, category, reason, withdraw_amount, balanced_amount) values('{}','{}','{}',{},{})".format(current,category,reason,withdrawAmount,depAmt)
                        cursorObject.execute(query) 
                        connectionObject.commit()
                    else:
                        print("Balanced Amount < Withdraw Amount !!")
                elif FunctionOption == 3:
                    print("Transaction Display")
                    print("1.Deposit Enquiry\n2.WithDraw Enquiry")
                    TransOption = int(input("Choose Option: "))
                    if TransOption == 1:
                        query = "select * from deposit"
                        cursorObject.execute(query)
                        os.system("cls")
                        print("Deposit Enquiry")
                        print("TRANSACTION ID\t\tDate-Time\t\tAMOUNT")
                        for row in cursorObject:
                            formatted_row = []
                            for i,item in enumerate(row):
                                if item is None:
                                    formatted_row.append("None")
                                elif i in [1]:  # Index 2 and 3 correspond to entry time and exit time
                                    formatted_row.append(item.strftime("%Y-%m-%d %H:%M:%S"))
                                else:
                                    formatted_row.append(item)
                            print("{:<23} {:<23} {}".format(*formatted_row))
                    elif TransOption == 2:
                        os.system("cls")
                        query = "select * from withdraw"
                        cursorObject.execute(query)
                        print("Withdraw Enquiry")
                        print("DATE-TIME\t\tCATEGORY\t\tREASON\t\tWITHDRAW\tBALANCE")
                        for i in cursorObject:
                            print("{date:<23} {category:<23} {reason:<15} {withdraw:<15} {balance:<15}".format(
                            date=i[0].strftime("%Y-%m-%d %H:%M:%S"),
                            category=i[1],
                            reason=i[2],
                            withdraw=i[3],
                            balance=i[4],))
                elif FunctionOption == 4:
                    os.system("cls")
                    print("BUdget Show")
                    print("1.Home Expense")
                    print("2.Personal Expense")
                    print("3.Petrol Expense")
                    print("4.Fuel Expense")
                    BUdgetOption = int(input("Enter the option: "))
                    if BUdgetOption == 1:
                        os.system("cls")
                        print("Showing Home expense")
                        query = "select * from withdraw where category = '{}'".format("Home")
                        cursorObject.execute(query)

                        print("DATE-TIME\t\tCATEGORY\t\tREASON\t\tWITHDRAW\tBALANCE")
                        for i in cursorObject:
                            if i != ():    
                                print("{date:<23} {category:<23} {reason:<15} {withdraw:<15} {balance:<15}".format(
                                date=i[0].strftime("%Y-%m-%d %H:%M:%S"),
                                category=i[1],
                                reason=i[2],
                                withdraw=i[3],
                                balance=i[4],))
                            else:
                                print("No Data Found")
                        
                    elif BUdgetOption == 2:
                        os.system("cls")
                        print("Showing Home expense")
                        query = "select * from withdraw where category = '{}'".format("Personal")
                        cursorObject.execute(query)

                        print("DATE-TIME\t\tCATEGORY\t\tREASON\t\tWITHDRAW\tBALANCE")
                        for i in cursorObject:
                            if i != ():    
                                print("{date:<23} {category:<23} {reason:<15} {withdraw:<15} {balance:<15}".format(
                                date=i[0].strftime("%Y-%m-%d %H:%M:%S"),
                                category=i[1],
                                reason=i[2],
                                withdraw=i[3],
                                balance=i[4],))
                            else:
                                print("No Data Found")
                        
                    elif BUdgetOption == 3:
                        os.system("cls")
                        print("Showing Home expense")
                        query = "select * from withdraw where category = '{}'".format("Petrol")
                        cursorObject.execute(query)

                        print("DATE-TIME\t\tCATEGORY\t\tREASON\t\tWITHDRAW\tBALANCE")
                        for i in cursorObject:
                            if i is not None:    
                                print("{date:<23} {category:<23} {reason:<15} {withdraw:<15} {balance:<15}".format(
                                date=i[0].strftime("%Y-%m-%d %H:%M:%S"),
                                category=i[1],
                                reason=i[2],
                                withdraw=i[3],
                                balance=i[4],))
                            if i is None:
                                print("No Data Found")
                                break
                        
                    elif BUdgetOption == 4:
                        os.system("cls")
                        print("Showing Home expense")
                        query = "select * from withdraw where category = '{}'".format("Debt")
                        cursorObject.execute(query)

                        print("DATE-TIME\t\tCATEGORY\t\tREASON\t\tWITHDRAW\tBALANCE")
                        for i in cursorObject:
                            if i != ():    
                                print("{date:<23} {category:<23} {reason:<15} {withdraw:<15} {balance:<15}".format(
                                date=i[0].strftime("%Y-%m-%d %H:%M:%S"),
                                category=i[1],
                                reason=i[2],
                                withdraw=i[3],
                                balance=i[4],))
                            else:
                                print("No Data Found")
                WantAgain = input("\nDo You want to Continue:(y/n): ")        
        else:
            print("Login Unsuccessfull")
    option = input("Want to continue: ")


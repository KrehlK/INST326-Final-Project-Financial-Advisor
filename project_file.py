import pandas as pd
import csv
from argparse import ArgumentParser

# ignore pandas chained assignment warning
pd.options.mode.chained_assignment = None

# constants for user input
MENU_CHOICES = {"display_all" : 1, "display_one" : 2, "deposit" : 3, "withdraw" : 4, "exit" : 5}

class Bank:
    """
    A bank's databse with customer account information
    
    Attributes:
        name(str): the name

    """
    
    def __init__(self, filepath):
        # read csv data into a pandas dataframe
        self.db = pd.read_csv(filepath,
                           index_col = "Account Number")


        
    def receipt(self):
        """
        prints out the status of the bank account
        
        Args:
            self: instance of receipt
        Side effects:
            print(): prints to terminal
        """
        #Abdul
        
    
    def credit(self, account):
        """
            This method uses the amount of money in a 
            users account and determines if they qualify for a credit card.

            Args:
                account:(user's account)

            Returns:
                A TRUE if they qualify or a FALSE if they don't? 
        """
        #stefan
        if self.account >= "500": # initialize self.account
            return True
        else:
            return False

    def checker(self, account_num):
        """
        stefan
    
        checks if the account number given is a part of the database
        returns  true or false
        if  false raise a error
        """
        try:
            self.db.loc[account_num]
            return True
        except KeyError:
            return False
            
            
    
    
class Customer:
    """
    Each customers information with a bank account 
    
    Attributes:
        account_number(int): user input
        bankdb: a row of Bank 
        phone(str):
        
    """
    def __init__(self, account_num, bankdb):
        if bankdb.checker(account_num):
            self.person =  bankdb.db.loc[account_num]
            self.balance = float(self.person["Balance"][1:].replace(',', ''))
        else:
            raise "You have put in the wrong numbers or you dont have an account with us try again"
    
    def withdraw(self, amount):
        """
        Withdraws money from the bank account
        
        """
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            # updates pandas dataframe cell for when customer data is printed
            self.person.loc["Balance"] = "${:.2f}".format(self.balance)
        
        
    def deposit(self, amount):
        """
        accesses the 
        
        Args:
            self:
            bank():
            
        """
        self.balance += amount
        # updates pandas dataframe cell for when customer data is printed
        self.person.loc["Balance"] = "${:.2f}".format(self.balance)
        
        
    def saving(self):
       """ 
       This Method will be used to keep track of the person’s saving. 
       In this option, the person will be able to input any other places 
       they may have their money saved. In this method, the person will also 
       have the option to input if they withdraw any money
       
       """
       
    def view_account(self):
        """
        michael
        view the current accoount
        """
        print(self.person)
        
def summary():
    """
    abdul
    a view of the bank database
    """
   
    import csv
    
    with open('INST326projectdata.csv') as csvfile:
        read_csv = csv.reader(csvfile)
    print(read_csv)

    for row in read_csv:
        print(row)
    

def main(filepath):
    b = Bank(filepath)
    customers = {}

    # create dictionary of Customer objects
    for account_num in b.db.index:
        customers[account_num] = Customer(account_num, b)

    repeat = True

    # repeatedly prompt menu until they request to exit
    while repeat:
        # prompt user for a choice
        print("Enter a choice:")
        print(f'{MENU_CHOICES["display_all"]}. Print Account Numbers')
        print(f'{MENU_CHOICES["display_one"]}. Print a Customer\'s Info')
        print(f'{MENU_CHOICES["deposit"]}. Make a Deposit')
        print(f'{MENU_CHOICES["withdraw"]}. Make a Withdrawal')
        print(f'{MENU_CHOICES["exit"]}. Exit')
        choice = 0

        # get user's choice
        try:
            choice = int(input())
        except:
            choice = 0

        # if they want to display account nums
        if choice == MENU_CHOICES["display_all"]:
            for x in b.db.index:
                try:
                    print(int(x))
                except ValueError:
                    print(x)
        # if they want to display one customer's info
        elif choice == MENU_CHOICES["display_one"]:
            try:
                account_num = int(input("Enter an account number to deposit to: "))
                customers[account_num].view_account()
            except ValueError:
                print("Invalid number entered.")
            except KeyError:
                print("Account not found.")
        elif choice == MENU_CHOICES["deposit"]:
            try:
                account_num = int(input("Enter an account number to deposit to: "))
                customers[account_num].deposit(float(input("Enter amount to deposit: ")))
            except ValueError:
                print("Invalid number entered.")
            except KeyError:
                print("Account not found.")
        elif choice == MENU_CHOICES["withdraw"]:
            try:
                account_num = int(input("Enter an account number to withdraw from: "))
                customers[account_num].withdraw(float(input("Enter amount to withdraw: ")))
            except ValueError:
                print("Invalid number entered.")
            except KeyError:
                print("Account not found.")
        elif choice == MENU_CHOICES["exit"]:
            repeat = False
    
# hard coded csv file name for now
main("data.csv")
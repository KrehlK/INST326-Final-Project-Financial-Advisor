import pandas as pd
import csv
from argparse import ArgumentParser

# constants for user input
MENU_CHOICES = {"display" : 1, "deposit" : 2, "withdraw" : 3, 5 : "exit"}

class Bank:
    """
    A bank's databse with customer account information
    
    Attributes:
        name(str): the name

    """
    
    def __init__(self, filepath):
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
            self.bank = bankdb
            self.person =  bankdb.db.loc[account_num]
        else:
            raise "You have put in the wrong numbers or you dont have an account with us try again"
    
    def withdraw():
        """
        Withdraws money from the bank account and adds it to the wallet
        
        """
        
        #michael
        
    def deposit(self, bank):
        """
        accesses the 
        
        Args:
            self:
            bank():
            
        """
        
            
        #krehl

        
        
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
   
    import csv
    
    with open('INST326projectdata.csv') as csvfile:
        read_csv = csv.reader(csvfile)
    print(read_csv)

    for row in read_csv:
        print(row)

   
    """
    abdul
    a view of the bank database
    """

def main(filepath):
    b = Bank(filepath)
    #Bob = Customer(112233445566, b)
    #Bob.view_account()

    repeat = True

    while repeat:
        print("Enter a choice:")
        print(f"1. Print Account Numbers")
        print(f"2. Make a Deposit")
        print(f"3. Make a Withdrawal")
        print(f"5. Exit")
        choice = 0

        try:
            choice = int(input())
        except:
            choice = 0

        if choice == MENU_CHOICES["display"]:
            for x in b.db.index:
                try:
                    print(int(x))
                except ValueError:
                    print(x)
        elif choice == 5:
            repeat = False
    
main("data.csv")
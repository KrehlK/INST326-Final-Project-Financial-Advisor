import pandas as pd
import csv

class Bank:
    """
    A bank with a person's bank account information
    
    Attributes:
        name(str): the name
        connections(set of Person): other ppl

    """
    def __init__(self, filepath):
        self.pd = csv.reader(filepath,
                           sep= "\t", index_col = "Account Number")
        """
        
        """
    
        

    def transaction(self, action):
        """
        an transaction that removes or adds money
        
        Args:
            self: instance of Bank
            action: a integer that can be negative or positive
        """
        self.balance = self.balance + action
        
    def reciept(self):
        """
        prints out the status of the bank account
        
        Args:
            self: instance of receipt
        Side effects:
            print(): prints to terminal
        """
        print(f"Account Summary\n" +
              "Account Owner: {name}\n" +
              "Account Number: {account_number}\n" +
              "Balance: {balance}")
        
    def saving(self):
       """ 
       This Method will be used to keep track of the person’s saving. 
       In this option, the person will be able to input any other places 
       they may have their money saved. In this method, the person will also 
       have the option to input if they withdraw any money
       
       """
    
    def credit(self, account):
        """
            This method uses the amount of money in a 
            users account and determines if they qualify for a credit card.

            Args:
                account:(user's account)

            Returns:
                A TRUE if they qualify or a FALSE if they don't? 
        """
            
    
    
class Customer:
    """
    Each customers information with a bank account 
    
    Attributes:
        account_number(int): user input
        bank_account: a row of Bank 
        phone(str):
        
    """
    def __init__(self, account_number, bank_account):
        self.account_number = bank_account["Account Number"]
        self.wallet = 0.0
        self.full_name = concat(bank_account["First Name"], " ",
                                bank_account["Last Name"])
        self.email = bank_account["Email"]
        self.phone = bank_account["Phone"]
        self.balance = bank_account["Balance"]
        self.credit = bank_account["Credit"]
        
    
    def withdraw():
        """
        Withdraws money from the bank account and adds it to the wallet
        """

    def deposit():
        """
        Deposits money into the bank account and removes it from the wallet
        """

def method():
    """
    michael
    view the current accoount
    """

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

def checker():
    """
    stefan
    
    checks if the account number given is a part of the database
    """
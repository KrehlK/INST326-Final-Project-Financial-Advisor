import pandas as pd
import csv
from argparse import ArgumentParser

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
    
        
    def reciept(self):
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
            
    
    
class Customer:
    """
    Each customers information with a bank account 
    
    Attributes:
        account_number(int): user input
        bankdb: a row of Bank 
        phone(str):
        
    """
    def __init__(self, account_number, bankdb):
        
        if checker(account_number) == True:
            self.person =  bankdb.loc[account_num]
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
       
    def view_account():
        """
        michael
        view the current accoount
        """
        
        print(f'Account Number: {self.account_number}')
        print(f'Name: {self.full_name}')
        print(f'Email: {self.email}')
        print(f'Phone: {self.phone}')
        print(f'Balance: {self.balance}')
        print(f'Credit: {self.credit}')
        
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
    returns  true or false
    if  false raise a error
    """

def main(filepath):
    
def parse_args(arglist):
    """ Process command line arguments.
    
    Expect one mandatory argument (a frequency) and one optional argument,
    preceded by "-a4" (the value to use as the frequency of A4).
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace.
    """
    parser = ArgumentParser()
    parser.add_argument("freq", type=float, help="a frequency in Hz")
    parser.add_argument("-a4", type=float, default=440.0,
                        help="frequency to use for A4")
    args = parser.parse_args(arglist)
    return args


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.freq, a4=args.a4)

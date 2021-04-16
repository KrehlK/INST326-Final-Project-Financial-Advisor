""" 
a test file to see if git is working
"""

class Bank:
    """
    A bank with a person's bank account information
    
    Attributes:
        name(str): the name
        connections(set of Person): other ppl

    """
    def __init__(self, filepath):
        db = ()
        with open(filpath, 'r', encoding= "UTF-8") as file:
            for line in file:
                line.split()
                name =  line[0] + line[1]
                account_number = line[2]
                balance = line[3]
                account = {"name": name, "Account Number": account_number, 
                           "balance": balance}
                db.append(account)
    
    def transaction(self, action):
        """
        an transaction that removes or adds money
        """
        self.balance = self.balance + action
        
    def display(self):
        print()
                
    
                
                
                
        
    
class Customer:
     """
    Each customers information with a bank account 
    
    Attributes:
        name(str): the name
        
    """
    
       
class Bank_account(Bank):
    
    
        
        
class saving(Bank):
    
def deposit account:

"""
    This will show each customers account balance, and any other accounts they have
    
    Attributes:
        name(str): the name
        num: account numbers 
          
    """


def deposit transactions:

"""
    This will show each customers transaction history.
    
    Attributes:
        name: account name
        num: dollar amount
          
    """


def withdrawal:
    
"""
    This will show each customers withdrawl
    
    Attributes:
        num: dollar amount
          
    """

def transfer:

"""
    This will show each customers transfer
    
    Attributes:
        name: account name
        num: dollar amount
          
    """


def spending tracker:

"""
    This will show how much each customer spends
    
    Attributes:
        name: account name
        num: dollar amount
        percent: the percentage amount of their spending
          
    """


def income to saving ratio:
    



def alerts:
    
    
"""
    This will alert customers if they have spend over their limit 

        Attributes:
        num: dollar amount
          
    """

def reward:
    
"""
    This will show each customer how much they have earned from their spending 

        Attributes:
        num: dollar amount
        point: amount of points they have earned 
          
    """


def schedule appointments: 
    
    """
    This allow customer to make appointment to meet with their advior

        Attributes:
        date: available dates
        time: availabe times and the duration
              
    """







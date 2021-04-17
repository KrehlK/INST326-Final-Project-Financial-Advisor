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
        print(f"Account Summary 
              Account Owner: {name} 
              Account Number: {account_number} 
              Balance: {balance}")
        
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
        name(str): the name
        
    """
    def __init__(name, bank_account):
        self.name = name
        self.wallet = 0.0
        self.bank_account = bank_account
    
    def withdraw():
        """
        Withdraws money from the bank account and adds it to the wallet
        """

    def deposit():
        """
        Deposits money into the bank account and removes it from the wallet
        """
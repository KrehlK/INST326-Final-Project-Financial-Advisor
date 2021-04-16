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
        
    def reciept(self):
        """
        Side effects:
            print(): prints to terminal
        """
        print(f"Account Summary 
              Account Owner: {name} 
              Account Number: {account_number} 
              Balance: {balance}")
        
    def saving(self):
        # for abdul: is the savings moreso transferring money
        # to savings or adding money?
    
    def credit:
        """
        1000
        *.8
        _____
        800> 200$ 
        return boolean 
        (yes)
        customer can apply credit card
        """
    
class Customer:
     """
    Each customers information with a bank account 
    
    Attributes:
        name(str): the name
        
    """
    def __init__():
    
       







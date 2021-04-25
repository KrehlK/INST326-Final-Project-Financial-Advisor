import pandas as pd


        
class Bank:
    """
    A bank with a person's bank account information
    
    Attributes:
        name(str): the name
        connections(set of Person): other ppl

    """
    def __init__(self, accountnumber):
        
        # to test collume to be search... ideially it will 
        search_firstname = accountnumber
        
        df = pd.read_csv("INST326projectdata.csv")
        
        # Choose entries with first name
        df_new = df[df['First Name'] == search_firstname]
        #This should change to account later, have to fix cvs format first.
        
        print("init")
        #print(str(self.data))
        
        print(df_new)
        
        self.account_number = df_new["Account Number"]
        self.first_name = df_new["First Name"]
        self.last_name =  df_new["Last Name"]
        self.email = df_new["Email"]
        self.phone = df_new["Phone"]
        self.balance = df_new["Balance"] 
        self.credit = df_new["Credit"]        
        self.credit_score = df_new["Credit Score"] 
        self.recurring_payments = df_new["Recurring Payments"] 
        
        
        print(self.last_name + " " + self.email )
    #this is a test
    
    
    def transaction(self):
        print("transaction")
        """
        an transaction that removes or adds money

        Args:
        self: instance of Bank
        action: a integer that can be negative or positive
        """
        #self.balance = self.balance + action



print("start here")
test1 = Bank("Michael")
test1.transaction()
#this is passing via name for now, change to 
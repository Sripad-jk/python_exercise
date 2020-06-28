class BankTransact():
    '''
    This class maintains the users credit balance account
    '''
    
    def __init__(self, amount=500):
        '''
        Initializes the bank roll by depositing default currency of 500
        '''
        self.amount = amount
    
    def withdraw(self, debit):
        '''
        Withdraws money of the said amount
        If no funds, returns 'Not enough funds'
        '''
        if(self.amount >= debit):
            self.amount = self.amount - debit
            print(f'Current Balance = {self.amount}')
        else:
            return('Not enough funds')
    
    def deposit(self, credit):
        '''
        The routine adds the money to the account
        '''
        self.amount = self.amount + credit
        print(f'Current Balance = {self.amount}')

    def current_balance(self):
        '''
        The routine displays current account balance
        '''
        return(self.amount)
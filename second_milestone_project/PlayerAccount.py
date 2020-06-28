from BankTransact import BankTransact
from PawnManager import PawnManager

class PlayerAccount(BankRoll, PawnManager):
    
    '''
    This class inherits the Bankroll class and PawnManager class to manage player accounts
    '''
    
    def __init__(self, gamer_type, amount):
        PawnManager.__init__(self, gamer_type)
        BankTransact.__init__(self, amount)
        self.total_sum  = 0
        self.betting_sum = 0
        
    def evaluate_pawns_value(self):
        '''
        This routine displays the current value of all pawns held by the player
        '''
        print(f'{self.gamer_type} value totals to:')
        for pawns in self.gamer_list:
            if(pawns[0] != 'ACE'):
                #Add all the value but exclude ACE 
                self.total_sum = self.total_sum + pawns[1]
            else:
                #Mark the ACE held status
                self.ACE_Held = True
                
        #Appropriate ACE accordingly        
        if(self.ACE_Held == True):
            #if the total value is less than 11
            if(self.total_sum < 11):
                self.total_sum = self.total_sum + 11
            ##else if the total value is greater than 11    
            else:
                self.total_sum = self.total_sum + 1
                
        print(f'Total Sum = {self.total_sum}')
        
    def place_bet(self, amount):
        '''
        This routine places bet from the players account
        '''
        if(amount < self.current_balance()):
            self.betting_sum = amount
            print(f'Successful bet placed')
        else:
            print('Not enough funds')
    
    def game_pay(self, game_result):
        '''
        This routine deposits or withdraws money based on gamer's victory or lose respectively 
        '''
        
        if('LOSE' == game_result):
            self.withdraw(self.betting_sum)
        else:
            self.deposit(self.betting_sum)
            
    
        
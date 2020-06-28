class PawnManager():
    '''
    This class manages the operation of pawn keeping. Displaying the held card.
    '''
    
    def __init__(self, gamer_type):
        '''
        The init routine initializes the pawn held to 0 and sets the gamer_type 
        to either dealer or player
        '''
        self.gamer_list = []
        self.gamer_type = gamer_type
        self.total_pawns_held = 0
        self.current_pawn = 0
    
    def push_card(self, pawn):
        '''
        The gamer list appends the pawn drawn
        '''
        self.gamer_list.append(pawn)
        self.total_pawns_held = len(self.gamer_list) 
        
    def display_gamer_card(self):
        '''
        This routine displays the card held by the player
        '''
        print(f'{self.gamer_type} holds: {self.gamer_list[self.current_pawn]}')
        if(self.current_pawn < (self.total_pawns_held - 1)):
            self.current_pawn = self.current_pawn + 1
            
    def display_all_card(self):
        '''
        This routine displays all cards held by the player
        '''
        print(f'{self.gamer_type} holds:')
        for pawns in self.gamer_list:
            print(f'{pawns}')
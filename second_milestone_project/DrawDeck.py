import random

class Card_Draw():
    
    '''
       This class helps in drawing cards
    '''
    
    #FaceCardList = ('ACE', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King')
    TilePackList = ('Hearts', 'Tiles', 'Clovers', 'Pikes')
    MasterDeck = {
            'Hearts': {'ACE':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King': 10},
            'Tiles' : {'ACE':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King': 10},
           'Clovers': {'ACE':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King': 10},
             'Pikes': {'ACE':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King': 10}
           }
    
    def __init__(self):
        
        '''
        The init routine here initializes the DeckPack from Master Deck
        '''
        Card_Draw.DeckPack = Card_Draw.MasterDeck
    
    def draw_card(self):
        
        '''
        This routine helps in drawing random cards. 
        Returns: Tuple( CardID as string,  CardVal as int )
        '''
        Tiles = []
        CardList = []
        Tiles.clear()
        CardList.clear()
        
        # List Tiles a random Tile
        TileSelect = random.choice(Card_Draw.TilePackList)
        
        #Find the available selection from Tiles list above
        for Card in Card_Draw.DeckPack[TileSelect].items(): 
            CardList.append(Card[0])
         
        #pick a random card
        CardID = random.choice(CardList)
        
        #Pop Selected Card
        CardVal = Card_Draw.DeckPack[TileSelect].pop(CardID)
        
        #return a Tuple with CardID as String & CardVal as face-value of card
        return(CardID, CardVal)

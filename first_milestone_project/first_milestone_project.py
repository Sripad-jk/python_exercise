TTT_Board = [' ']*10

def init_board():
	'''
    This function initializes the board 
	'''
    global TTT_Board 
    TTT_Board = [' ']*10
    TTT_Board[0] = '#'

def read_cell(pos):
	'''
    This function is used to read a cell in the TTT board
	'''
    global TTT_Board
    return(TTT_Board[pos])

def write_cell(cell_pos, mark):
	'''
    This function is used to write a cell in the TTT board
	'''
    global TTT_Board
    TTT_Board[cell_pos] = mark

def check_empty_cell(pos):
	'''
    This function checks if the passed cell is empty 
    Return TRUE -> cell empty
    Return FALSE -> Cell not empty
	'''
    if(read_cell(pos) == ' '):
        return True
    else:
        return False

def examine_cell_preoccupied(pos):
    if (check_empty_cell(pos) == True):
        return True
    else:
        print('Cell Taken Please enter a different cell')
        return False


def is_board_full():
    boolval = True
    for i in range(1, 10):
        if(True == check_empty_cell(i)):
            boolval = False
    return boolval

def determine_victory(mark):
    win_declared = False
    win_pattern = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9))
    for tuplet in win_pattern:
        if(read_cell(tuplet[0]) == mark) and (read_cell(tuplet[1]) == mark) and (read_cell(tuplet[2]) == mark):
            win_declared = True
            break
    return win_declared

import random

def toss():

    val = random.randint(0, 1)
    return val

def user_input(val):
    char = ''
    val1 = ''
    val2 = ''
    mydict = {}
    print(f' Player-{val+1} please enter your marker choice X or O:')
    while(char.upper() != 'X') and (char.upper() != 'O'):
        char = input()
        if(char.upper() == 'X'):
            if(val == 0):
                val1 = char.upper()
                val2 = 'O'
                val = "Player_1"
            else:
                val1 = 'O' 
                val2 = char.upper()
                val = "Player_2"
                
        elif(char.upper() == 'O'):
            if(val == 0):
                val1 = char.upper()
                val2 = 'X'
                val = "Player_1"
            else:
                val1 = 'X' 
                val2 = char.upper()
                val = "Player_2"
        else:
            print('Please enter a valid choice X or O')
            
    mydict["Current_Player"] = val
    mydict["Player_1"] = val1
    mydict["Player_2"] = val2
    print(f'Player-1 is {mydict["Player_1"]}')
    print(f'Player-2 is {mydict["Player_2"]}')
    
    return(mydict)

def input_cell(val, marker):
    cell_val = 0
    correct_cell = False
    print(f'{val} please enter your cell choice - 1 to 9:')
    while (correct_cell == False):
        cell_val = int(input())
        if(cell_val < 1) or (cell_val >9):
            print('Please choose between 1 & 9')
        elif(not examine_cell_preoccupied(cell_val)):
            print('Cell taken please choose a different cell position')
        else:
            correct_cell = True
            write_cell(cell_val, marker)
            display_board()
    return(correct_cell)

from IPython.display import clear_output

def display_board():
    clear_output()
    print('|'+read_cell(7)+'|'+read_cell(8)+'|'+read_cell(9)+'|')
    print('|'+read_cell(4)+'|'+read_cell(5)+'|'+read_cell(6)+'|')
    print('|'+read_cell(1)+'|'+read_cell(2)+'|'+read_cell(3)+'|')

def game_play():
    
    Game_Over = False
    my_dict = {}
    char = ''
    player_name = ''
    player_mark = ''
    valid_char = False
    reinvite = False
    init_board()
    ply_val = toss()
    my_dict = user_input(ply_val)
    while(reinvite != True):
        if(is_board_full() != True):
            player_name = my_dict['Current_Player']
            player_mark = my_dict[my_dict['Current_Player']]
            print(f'{player_name}, {player_mark}')
            if(input_cell(player_name, player_mark ) == True):
                if(determine_victory(player_mark) == True):
                    print(f'{player_name} won the game')
                    reinvite  = True
                else:
                    if(my_dict['Current_Player'] == 'Player_1'):
                        my_dict['Current_Player'] = 'Player_2'
                    else:
                        my_dict['Current_Player'] = 'Player_1'
        else:
            reinvite  = True
            if(determine_victory(my_dict[my_dict['Current_Player']]) != True):
                print('No one wins')
            else:
                player_name = my_dict['Current_Player']
                print(f'{player_name} won the game')
        
    if(reinvite == True):
        print("Do you wish to play again, type Y or N")
        while(valid_char == False):
            char = input()
            if(char.upper() == 'N'):
                Game_Over = True
                valid_char = True
                print("Auf Wiedersehen")
            elif(char.upper() == 'Y'):
                valid_char = True
                print('Lets Play again! \nReloading......!')
            else:
                print("please enter Y or N only")
                valid_char = False
        
    return(Game_Over)


def TTT_Board_Game():
    while(game_play() != True):
        pass

TTT_Board_Game()
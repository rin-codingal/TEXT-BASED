#Tic Tac Toe

''' 
    We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. 
'''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' 
    We will have to print the updated board after every move in the game and thus we will make a function 
    in which     we'll define the printBoard function so that we can easily print the board everytime by 
    calling this function. 
'''
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

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 
    count = 

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," +  + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = 
            count += 
        else:
            print("")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                printBoard()
                print("")                
                print()                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                printBoard()
                print("")                
                print()
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                printBoard()
                print("")                
                print()
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                printBoard()
                print("")                
                print()
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                printBoard()
                print("")                
                print()
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                printBoard()
                print("")                
                print()
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                printBoard()
                print("")                
                print()
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                printBoard()
                print("")                
                print()
                break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("")                
            print("")

        # Now we have to change the player after every move.
        if turn ==:
            turn = 
        else:
            turn =         
    
    restart = input("Do want to play Again?(y/n)")
    if restart ==  or restart == :  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()
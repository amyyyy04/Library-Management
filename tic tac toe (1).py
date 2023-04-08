#Implementation of Two Player Tic-Tac-Toe game in Python.

''' We will make the board using dictionary 
    in which keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be empty space and then after every move 
    we will change the value according to player's choice of move. '''


print ("❋❃❋❃❋❃❋WELCOME TO THE TIC-TAC-TOE GAME!❋❃❋❃❋❃❋ ")

print()

print ("Players 'X' and 'O', you have to follow the given rules: ")

print()

print("1. You cannot change your choice after hitting the 'ENTER' button.")
print("2. A player wins when he/she completes either a row/column or a diagonal.")
print("3. You cannot chose a position once it is taken by your opponent.")
print("4. No one wins if a row/column/diagonal is NOT completed. :) obvious :) ")

print()

theBoard = {'21': ' ','22': ' ','23': ' ','24': ' ','25': ' ',
            '16': ' ','17': ' ','18': ' ','19': ' ','20': ' ',
            '11': ' ', '12': ' ', '13': ' ', '14': ' ', '15': ' ',
            '6': ' ', '7': ' ', '8': ' ','9': ' ','10': ' ',
            '1': ' ', '2': ' ', '3': ' ', '4': ' ', '5': ' '}

#First we create an empty list
board_keys = []

#Then we will append all the keys of theBoard dictionary into it

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''


print(" 21 | 22 | 23 | 24 | 25 ")
print("----+----+----+----+----")
print(" 16 | 17 | 18 | 19 | 20 ")
print("----+----+----+----+----")
print(" 11 | 12 | 13 | 14 | 15 ")
print("----+----+----+----+----")
print(" 6  | 7  | 8  | 9  | 10 ")
print("----+----+----+----+----")
print(" 1  | 2  | 3  | 4  | 5 ") 







def printBoard(board):
    print(board['21'] + '   |   ' + board['22'] + '|  ' + board['23'] + ' | '+ board['24'] +'  |'+ board['25'])
    print('----+----+----+----+----')
    print(board['16'] + '   |   ' + board['17'] + '|  ' + board['18'] + ' | '+board['19']+ '  |' + board['20'])
    print('----+----+----+----+----')
    print(board['11'] + '   |   ' + board['12'] + '|  ' + board['13'] + ' | '+ board['14'] +'  |'+ board['15'])
    print('----+----+----+----+----')
    print(board['6'] + '   |   ' + board['7'] + '|  ' + board['8'] + ' | '+ board['9'] +'  |'+ board['10'])
    print('----+----+----+----+----')
    print(board['1'] + '   |   ' + board['2'] + '|  ' + board['3'] + ' | ' + board['4'] + '  |'+ board['5'])

    

# Now we'll write the main function which has all the gameplay functionality.
def game():

    #Here first we will assign 'X' to player 1 
    turn = 'X'
    count = 0


    for i in range(25):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 9 moves. 
        if count >= 9:
            # across the top
            if theBoard['21'] == theBoard['22'] == theBoard['23'] == theBoard['24'] == theBoard['25'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            
            # across the second row
            elif theBoard['16'] == theBoard['17'] == theBoard['18'] == theBoard['19'] == theBoard['20'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            
            # across the middle
            elif theBoard['11'] == theBoard['12'] == theBoard['13'] == theBoard['14'] == theBoard['15'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            
            # across the last second row
            elif theBoard['6'] == theBoard['7'] == theBoard['8'] == theBoard['9'] == theBoard['10'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            
            # across the last row
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] == theBoard['4'] == theBoard['5'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            
            # down the right side
            elif theBoard['5'] == theBoard['10'] == theBoard['15'] == theBoard['20'] == theBoard['25'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # down the 4th column
            elif theBoard['4'] == theBoard['9'] == theBoard['14'] == theBoard['19'] == theBoard['24'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # down the middle column
            elif theBoard['3'] == theBoard['8'] == theBoard['13'] == theBoard['18'] == theBoard['23'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # down the 2nd column
            elif theBoard['2'] == theBoard['7'] == theBoard['12'] == theBoard['17'] == theBoard['22'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # down the left side
            elif theBoard['1'] == theBoard['6'] == theBoard['11'] == theBoard['16'] == theBoard['21'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # diagonal
            elif theBoard['1'] == theBoard['7'] == theBoard['13'] == theBoard['19'] == theBoard['25'] != ' ':
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break

            # diagonal
            elif theBoard['5'] == theBoard['9'] == theBoard['13'] == theBoard['17'] == theBoard['21'] != ' ':
                printBoard(theBoard)
                print("\nGame Over!\n")                
                print(" **** " +turn + " won. ****")

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 25:
            print("\nGame Over!\n")                
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    # Now we will ask if player wants to restart the game or not.
    
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":  
        for key in board_keys:
            theBoard[key] = " "

        game()

if __name__ == "__main__":
    game()

game_board= { '1': ' ', '2': ' ', '3': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '7': ' ', '8': ' ', '9': ' '}

keys = []
for key in game_board:
    keys.append(key)

print("Location Index: \n")
print('1' + '|' + '2' + '|' + '3')
print('-----')
print('4' + '|' + '5' + '|' + '6')
print('-----')
print('7' + '|' +'8' + '|' +  '9')
print("\n")

def display_board(board):
    
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-----')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-----')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print("\n")

def maingame():
    player= 'x'
    count= 0

    for i in range(10):
        display_board(game_board)
        print(player + " it is your turn. Enter location: ")
        loc= input()

        if game_board[loc]== ' ':
            game_board[loc] = player
            count= count + 1
        else:
            print("Location is not empty. Choose an alternative ")
            continue

        if count>=5 :
            if  game_board['1'] == game_board['2'] == game_board['3'] != ' ': # row1
                display_board(game_board)
                print(player + " is the winner! ")                
                break
            elif game_board['4'] == game_board['5'] == game_board['6'] != ' ': # row2
                display_board(game_board)
                print(player + " is the winner! ")
                break
            elif game_board['7'] == game_board['8'] == game_board['9'] != ' ': # row3
                display_board(game_board)
                print(player + " is the winner! ")
                break
            elif game_board['1'] == game_board['4'] == game_board['7'] != ' ': # col1
                display_board(game_board)
                print(player + " is the winner! ")
                break
            elif game_board['2'] == game_board['5'] == game_board['8'] != ' ': # col2
                display_board(game_board)
                print(player + " is the winner! ")
                break
            elif game_board['3'] == game_board['6'] == game_board['9'] != ' ': # col3
                display_board(game_board)
                print(player + " is the winner! ")
                break 
            elif game_board['3'] == game_board['5'] == game_board['7'] != ' ': # diag2
                display_board(game_board)
                print(player + " is the winner! ")
                break
            elif game_board['1'] == game_board['5'] == game_board['9'] != ' ': # diag1
                display_board(game_board)
                print(player + " is the winner! ")
                break 

        if count == 9:  

            print("Nobody wins. It's a tie ")
            break

        if player =='x':
            player = 'o'
        else:
            player = 'x'        
    

maingame()
       

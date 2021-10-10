print("\n ********** WELCOME TO TIC-TAC-TOE GAME **********\n")
print("         X | 0 | X    1 | 2 | 3")
print("         - - - - - -  - - - - - -")
print("         X | 0 | X    4 | 5 | 6 ")
print("         - - - - - -  - - - - - -")
print("         X | 0 | X    7 | 8 | 9 \n\n")

winning_possibilities = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

playground = ['- | - | -', '- - - - -', '- | - | -', '- - - - -', '- | - | -']

print("***** YOUR PLAYGROUND *****\n\n")
for line in playground:
    print(f"        {line}")
print("\n\n\n")

playground_first_line = playground[0].split(" ")
playground_second_line = playground[2].split(" ")
playground_third_line = playground[4].split(" ")


def show_game():
    print("\n\n")
    for lines in playground_first_line:
        print(f"    {lines}", end=" ")
    print("\n-----------------------------------\n")
    for lines in playground_second_line:
        print(f"    {lines}", end=" ")
    print("\n-----------------------------------\n")
    for lines in playground_third_line:
        print(f"    {lines}", end=" ")
    print("\n\n")


def make_move(player_no, player_move):
    if player_no == 1:
        symbol_of_player = 'X'
    else:
        symbol_of_player = '0'

    if player_move == 1:
        playground_first_line[0] = symbol_of_player
    elif player_move == 2:
        playground_first_line[2] = symbol_of_player
    elif player_move == 3:
        playground_first_line[4] = symbol_of_player
    elif player_move == 4:
        playground_second_line[0] = symbol_of_player
    elif player_move == 5:
        playground_second_line[2] = symbol_of_player
    elif player_move == 6:
        playground_second_line[4] = symbol_of_player
    elif player_move == 7:
        playground_third_line[0] = symbol_of_player
    elif player_move == 8:
        playground_third_line[2] = symbol_of_player
    elif player_move == 9:
        playground_third_line[4] = symbol_of_player


def check_won(player):
    if player == "player1":
        for win_move in winning_possibilities:
            if (win_move[0] in player1_old_moves) and \
                    (win_move[1] in player1_old_moves) and \
                    (win_move[2] in player1_old_moves):
                return True
        return False
    elif player == "player2":
        for win_move in winning_possibilities:
            if (win_move[0] in player2_old_moves) and \
                    (win_move[1] in player2_old_moves) and \
                    (win_move[2] in player2_old_moves):
                return True
        return False


is_game_on = True
move_no = 0
total_old_moves = []
player1_old_moves = []
player2_old_moves = []

while is_game_on and move_no < 9:
    try:
        player1_move = int(input("Player1(X): \n"))
    except ValueError:
        print("You are allowed to write only numbers!")
        print("If you do this again, game will end!\n")
        player1_move = int(input("Player1(X): \n"))
    finally:
        if player1_move > 9 or player1_move < 1:
            print("You are allowed to write numbers between 1-9!")
            print("If you do this again, game will end!\n")
            player1_move = int(input("Player1(X): \n"))
        if player1_move in total_old_moves:
            print("Wrong move!, Second player won!")
            break
        else:
            total_old_moves.append(player1_move)
            player1_old_moves.append(player1_move)
        make_move(player_no=1, player_move=player1_move)
        move_no += 1
        if check_won(player="player1"):
            show_game()
            print("******** PLAYER 1 WON! ********")
            break
        show_game()

    try:
        player2_move = int(input("Player2(0): \n"))
    except ValueError:
        print("You are allowed to write only numbers!")
        print("If you do this again, game will end!\n")
        player2_move = int(input("Player2(0): \n"))
    finally:
        if player2_move > 9 or player2_move < 1:
            print("You are allowed to write numbers between 1-9!")
            print("If you do this again, game will end!\n")
            player2_move = int(input("Player1(X): \n"))
        if player2_move in total_old_moves:
            print("Wrong move!, First player won!")
            break
        else:
            total_old_moves.append(player2_move)
            player2_old_moves.append(player2_move)
        make_move(player_no=2, player_move=player2_move)
        move_no += 1
        if check_won(player="player2"):
            show_game()
            print("******** PLAYER 2 WON! ********")
            break
        show_game()
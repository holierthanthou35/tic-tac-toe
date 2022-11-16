player_1_sign = None
player_2_sign = None
turn = "Player 1"
is_game_over = False

game_status = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
cell_remaining = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def print_welcome():
    print("Welcome to Tic-Tac-Toe!")


def choose_sign():
    global player_1_sign
    global player_2_sign
    is_correct = False

    while not is_correct:
        player_1_sign = input("Player 1, please choose your sign (X or O): ")
        if player_1_sign != 'X' and player_1_sign != 'O':
            print("Uh Oh! Please enter a correct character!")
        else:
            is_correct = True

    if player_1_sign == 'X':
        player_2_sign = 'O'
    else:
        player_2_sign = 'X'

    print(f"Player 1 Sign: {player_1_sign}")
    print(f"Player 2 Sign: {player_2_sign}")


def print_turn():
    print(f"{turn}'s turn!")


def print_game():
    print("   |   |   ")
    print(f" {game_status[0]} | {game_status[1]} | {game_status[2]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_status[3]} | {game_status[4]} | {game_status[5]} ")
    print("   |   |   ")
    print("---|---|---")
    print("   |   |   ")
    print(f" {game_status[6]} | {game_status[7]} | {game_status[8]} ")
    print("   |   |   ")


def position_choice():
    choice = 'wrong'

    while choice not in (cell_remaining):
        choice = input(
            "Please enter the position you want to play your mark in (1 - 9): ")

        if not choice.isdigit():
            print("Err! Are you sure that's a correct position?")
            continue
        else:
            choice = int(choice) - 1

        if choice not in cell_remaining:
            print("Err! Are you sure that's a correct position?")

    return choice


def change_status(position):
    global turn
    if turn == "Player 1":
        game_status[position] = player_1_sign
        turn = "Player 2"
    else:
        game_status[position] = player_2_sign
        turn = "Player 1"
    index = cell_remaining.index(position)
    cell_remaining.pop(index)

def display_tie():
    print("The game has been tied! Thanks for playing!")
    print_game()


def display_win():
    print(f"CONGRATS! {turn} won the game!!!")
    print_game()


def check_tie():
    flag = True
    global is_game_over
    for cell in game_status:
        if cell == ' ':
            flag = False
    if flag:
        is_game_over = True
        display_tie()
    

def check_win():
    global is_game_over
    if game_status[0] == game_status[3] == game_status[6] != ' ' or game_status[1] == game_status[4] == game_status[7] != ' ' or game_status[2] == game_status[5] == game_status[8] != ' ' or game_status[0] == game_status[1] == game_status[2] != ' ' or game_status[3] == game_status[4] == game_status[5] != ' ' or game_status[6] == game_status[7] == game_status[8] != ' ' or game_status[0] == game_status[4] == game_status[8] != ' ' or game_status[2] == game_status[4] == game_status[6] != ' ':
        is_game_over = True
        display_win()


def play_game():
    print_welcome()
    choose_sign()

    while not is_game_over:
        print_turn()
        print_game()
        position = position_choice()
        change_status(position)
        check_win()
        check_tie()


play_game()

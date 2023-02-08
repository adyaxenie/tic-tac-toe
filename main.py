game_board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
picked_spots = []


def player_place(turn):
    string = ""
    if turn == 0:
        string = "X"
    elif turn == 1:
        string = "O"

    move = input(f"Place an {string} (between 1 and 3) ex:'32': ")
    if len(move) != 2 or not int:
        print("Not a valid input, example would be '12'.")
        return player_place(turn)

    a = int(move[0])
    b = int(move[1])
    if a and b > 3 or a and b < 1:
        print("Invalid placement.")
    elif [a, b] in picked_spots:
        print("Can't place here. Try again.")
        return player_place(turn)
    else:
        picked_spots.append([a, b])
        game_board[a - 1][b - 1] = string
        game_display()


def game_display():
    board = ""
    for i in range(3):
        board += f"{game_board[i][0]}|{game_board[i][1]}|{game_board[i][2]}\n"
    print(board)


def check_win(player):
    for i in game_board:
        if i[0] == i[1] == i[2] == player:
            print(f"{player} wins!")
            return True
    for i in range(3):
        if game_board[0][i] == game_board[1][i] == game_board[2][i] == player:
            print(f"{player} wins!")
            return True
        if game_board[0][0] == game_board[1][1] == game_board[2][2] == player:
            print(f"{player} wins!")
            return True
        if game_board[0][2] == game_board[1][1] == game_board[2][0] == player:
            print(f"{player} wins!")
            return True


game_display()
game_on = True
while game_on:
    player_place(0)
    if check_win("X"):
        game_on = False
        break
    player_place(1)
    if check_win("O"):
        game_on = False

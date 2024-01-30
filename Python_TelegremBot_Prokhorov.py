play_board = [[],[],[]]
def draw_board(board):
    counter = 0
    for i in range(3):
        print(' |'.join(board[i]))
        counter += 1
        if counter == 3:
            break
        else:
            print("--------")
def ask_move(player,board):
    x = int(input(f"{player}, Введите x координату : "))
    y = int(input(f"{player}, Введите y координату : "))
    if (0 <= x <= 2) and (0 <= y <= 2) and (board[x][y] == " "):
        # если свободно, вовзращаем координаты
        return (x,y)
    else:
        print("Это место занято, попробуйте другое.")
        ask_move(player, board)
def make_move(player,board,x,y):
    # проверить, что клетка свободна
    if board[x][y] != " ":
        print("Клетка занята")
        return False
    # если клетка свободна, записать ход
    board[x][y] = player
    return True
def check_win(player, board):
    for i in range(3):
        if board[i] == [player,player,player]:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def ask_and_make_move(player, board):
    x,y = ask_move(player,board)
    make_move(player,board,x,y)

def tic_tac_toe():
    while True:
        board = [[" " for i in range(3)] for j in range(3)]
        player = 'X'
        while True:
            draw_board(board)
            ask_and_make_move(player,board)
            if check_win(player,board):
                print(f'{player} выиграл!')
                break
            tie_game = False
            for row in board:
                for cell in row:
                    if cell == ' ':
                        tie_game = True
            if not tie_game:
                break
            player = 'O' if player == 'X' else 'X'
        restart = input("Хотите сыграть еще раз? (y/n) ")
        if restart.lower() != 'y':
            break

tic_tac_toe()


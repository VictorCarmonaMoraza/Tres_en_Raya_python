## Tablero
board =[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

## Funcion Ganador
def check_winner(board):
    # Revisar filas
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # Revisar columnas
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]
    # Revisar diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]
    return None

##Empate
def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

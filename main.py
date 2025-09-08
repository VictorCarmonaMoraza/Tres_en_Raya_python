import tkinter as tk

## Tablero
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
current_player = 'X'

## Crear ventana principal
window = tk.Tk()
window.title("Tres en raya")
window.geometry("400x400")

## Crear etoiqueta de resultado
result_label = tk.Label(window, text=f"Turno del jugador {current_player}", font=("Arial", 16))
result_label.grid(row=0, column=0, columnspan=3)

buttons = [[None for _ in range(3)] for _ in range(3)]


def reset_game():
    global current_player, board
    current_player = 'X'
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    result_label.config(text=f"Turno del jugador X")
    for row in buttons:
        for button in row:
            button.config(text=' ', state="normal")


def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state="disabled")


def on_click(row, col):
    global current_player

    ## Verificar si la celda esta vacia
    if buttons[row][col]["text"] == ' ':
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player
        board[row][col] = current_player

        ## Verificar ganador
        winner = check_winner(board)
        if winner:
            result_label.config(text=f"Jugador {winner} gana!")
            disable_buttons()
        elif is_draw(board):
            result_label.config(text="Empate!")
        else:
            current_player = "0" if current_player == "X" else "X"
            result_label.config(text=f"Turno del jugador {current_player}")


## Crear tablero de botones
def create_board():
    for row in range(3):
        for col in range(3):
            buttons[row][col] = tk.Button(window, text=' ', font=('Arial', 24), width=5, height=2,
                                          command=lambda r=row, c=col: on_click(r, c))
            buttons[row][col].grid(row=row + 1, column=col)


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


create_board()
reset_button = tk.Button(window, text="Reset", font=("Arial", 14), command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

window.mainloop()

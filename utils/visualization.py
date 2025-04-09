# utils/visualization.py
import matplotlib.pyplot as plt
import numpy as np

def plot_board(board, title="Tablero"):
    board_array = np.array(board)
    fig, ax = plt.subplots()
    ax.matshow(board_array, cmap="Blues")
    for i in range(len(board)):
        for j in range(len(board)):
            ax.text(j, i, str(board[i][j]), va="center", ha="center", color="black")
    plt.title(title)
    return fig

def plot_queens(board, title="Tablero de N Reinas"):
    board_array = np.array(board)
    fig, ax = plt.subplots()
    ax.matshow(board_array, cmap="Blues")
    for i in range(len(board)):
        for j in range(len(board)):
            text = "Q" if board[i][j] == 1 else "."
            ax.text(j, i, text, va="center", ha="center", color="black")
    plt.title(title)
    return fig
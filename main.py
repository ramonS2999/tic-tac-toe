import math
import random

# --- Configurações globais ---
PLAYERS = ["X", "O"]  # Humano = X, Bot = O
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
    [0, 4, 8], [2, 4, 6]              # diagonais
]
COLORS = {"X": "\033[91mX\033[0m", "O": "\033[94mO\033[0m"}

# --- Funções auxiliares ---
def draw(board):
    print()
    for i in range(0, 9, 3):
        row = " | ".join(
            COLORS.get(board[j], str(j+1)) if board[j] != " " else str(j+1)
            for j in range(i, i+3)
        )
        print(row)
        if i < 6:
            print("-" * 10)

def win(board, player):
    return any(all(board[pos] == player for pos in combo) for combo in WINNING_COMBOS)

def is_full(board):
    return all(cell != " " for cell in board)

# --- Algoritmo Minimax ---
def minimax(board, depth, is_maximizing):
    if win(board, "O"):  # Bot
        return 1
    if win(board, "X"):  # Humano
        return -1
    if is_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(board, depth + 1, False)
                board[i] = " "
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(board, depth + 1, True)
                board[i] = " "
                best_score = min(score, best_score)
        return best_score

def best_move(board, difficulty="hard"):
    if difficulty == "easy":
        moves = [i for i, v in enumerate(board) if v == " "]
        return random.choice(moves)
    elif difficulty == "medium":
        if random.random() < 0.5:
            moves = [i for i, v in enumerate(board) if v == " "]
            return random.choice(moves)
    best_score = -math.inf
    move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, 0, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                move = i
    return move

# --- Jogo Principal ---
def main():
    board = [" "] * 9
    turn = 0

    print("=== 🎮 Jogo da Velha ===")
    mode = input("Escolha o modo de jogo:\n1 - Jogador vs Bot\n2 - Jogador vs Jogador\n> ").strip()
    if mode not in ["1", "2"]:
        mode = "1"

    if mode == "1":
        print("Você é o Jogador X. O Bot é o Jogador O.")
        difficulty = input("Escolha a dificuldade [easy / medium / hard]: ").strip().lower()
        if difficulty not in ["easy", "medium", "hard"]:
            difficulty = "medium"
    else:
        print("Modo 2 jogadores selecionado.")

    while True:
        draw(board)
        current_player = PLAYERS[turn % 2]

        if mode == "2" or (mode == "1" and current_player == "X"):  # humano
            move = input(f"\nJogador {current_player}, escolha uma posição [1-9]: ")
            if not move.isdigit() or int(move) not in range(1, 10):
                print("❌ Entrada inválida! Digite um número entre 1 e 9.")
                continue
            pos = int(move) - 1
            if board[pos] != " ":
                print("❌ Posição já ocupada! Escolha outra.")
                continue
        else:  # Bot
            pos = best_move(board, difficulty)
            print(f"\n🤖 Bot ({current_player}) escolheu a posição {pos+1}")

        board[pos] = current_player
        turn += 1

        if win(board, current_player):
            draw(board)
            print(f"🎉 Jogador {current_player} venceu no turno {turn}! 🏆")
            break
        elif is_full(board):
            draw(board)
            print("😥 Deu velha!")
            break

if __name__ == "__main__":
    main()

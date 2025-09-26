# --- Configurações globais ---
PLAYERS = ["X", "O"]
WINNING_COMBOS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # linhas
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # colunas
    [0, 4, 8], [2, 4, 6]              # diagonais
]
COLORS = {"X": "\033[91mX\033[0m", "O": "\033[94mO\033[0m"}


# --- Funções utilitárias ---
def draw(board):
    """Mostra o tabuleiro, numerando as casas vazias."""
    print()
    for i in range(0, 9, 3):
        row = " | ".join(COLORS.get(board[j], str(j+1)) if board[j] != " " else str(j+1) for j in range(i, i+3))
        print(row)
        if i < 6:
            print("-" * 10)

def win(board):
    """Verifica se existe uma combinação vencedora."""
    return any(board[a] != " " and board[a] == board[b] == board[c] for a, b, c in WINNING_COMBOS)

def get_move(board, current_player):
    """Solicita e valida a jogada do jogador."""
    while True:
        move = input(f"\nJogador {current_player}, escolha uma posição [1-9]: ")

        if not move.isdigit() or int(move) not in range(1, 10):
            print("❌ Entrada inválida! Digite um número entre 1 e 9.")
            continue

        pos = int(move) - 1
        if board[pos] != " ":
            print("❌ Posição já ocupada! Escolha outra.")
            continue

        return pos

# --- Função principal ---
def main():
    board = [" "] * 9
    turn = 0

    while True:
        draw(board)
        current_player = PLAYERS[turn % 2]

        pos = get_move(board, current_player)
        board[pos] = current_player
        turn += 1

        if win(board):
            draw(board)
            print(f"🎉 Jogador {current_player} venceu no turno {turn}! 🏆")
            break
        elif turn == 9:
            draw(board)
            print("😥 Deu velha!")
            break

# --- Executa o jogo ---
if __name__ == "__main__":
    main()

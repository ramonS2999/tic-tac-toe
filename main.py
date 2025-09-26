def main():
    board_game = [" "] * 9
    players = ["X", "O"]
    turn = 0

    while True:
        draw(board_game)
        current_player = players[turn % 2]

        print(f"\nTurno [{turn + 1}] - Jogador {current_player}")

        # Pede a jogada
        move = input("Digite uma posição disponível no intervalo de [1-9]: ")

        # Validação
        if not move.isdigit() or int(move) not in range(1, 10):
            print("❌ Entrada inválida! Digite um número entre 1 e 9.")
            continue

        pos = int(move) - 1
        if board_game[pos] != " ":
            print("❌ Posição já ocupada! Escolha outra.")
            continue

        # Marca jogada
        board_game[pos] = current_player
        turn += 1

        # Verifica vitória
        if win(board_game):
            draw(board_game)
            print(f"🎉 Jogador {current_player} venceu no turno {turn}! 🏆")
            break

        # Verifica empate
        if turn == 9:
            draw(board_game)
            print("😥 Deu velha!")
            break

# Verifica se teve vencedor
def win(board_game):
    # Todas as combinações possíveis de vitória
    winning_combinations = [
        [0, 1, 2],  # linha 1
        [3, 4, 5],  # linha 2
        [6, 7, 8],  # linha 3
        [0, 3, 6],  # coluna 1
        [1, 4, 7],  # coluna 2
        [2, 5, 8],  # coluna 3
        [0, 4, 8],  # diagonal principal
        [2, 4, 6]   # diagonal secundária
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board_game[a] != " " and board_game[a] == board_game[b] == board_game[c]:
            return True

    return False

# Desenha o tabuleiro com separadores e cores para X e O
def draw(board):
    COLORS = {"X": "\033[91mX\033[0m", "O": "\033[94mO\033[0m", " ": " "}
    print()
    for i in range(0, 9, 3):
        row = " | ".join(COLORS[cell] for cell in board[i:i+3])
        print(row)
        if i < 6:
            print("-" * 10)

# Chamado o jogo
main()

def main():
    # Variávei de inicialização
    board_game = [" "] * 9
    char = ["X", "O"]
    plyer_turn = True
    turn = 0
    turn_max = 9
    player_winner = plyer_turn

    while True:
        if not is_tied(turn, turn_max, board_game):
            print(f"Turno: Jogador {str(getPayer(plyer_turn))}")
            print(f"Turno [{turn + 1}]")
            check = input("Digite uma posição disponível no intervalo de [1-9]: ")

            if check_list_all(board_game, turn, check, turn_max):
                board_game[int(check) - 1] = char[getPayer(plyer_turn)- 1]
                player_winner = plyer_turn
                plyer_turn = not plyer_turn
                turn += 1
                draw(board_game)

            if win(board_game):
                print(f"O Jogador {getPayer(player_winner)} Venceu no Turno [{turn}]!  🎉 🏆 🤩")
                break
        else:
            draw(board_game)
            print("VELHA 😥")
            break

# Verifica se teve vencedor
def win(board_game):
    hor = ver = dgl = 0

    for j in range(3):
        # Hirizontal lines
        if board_game[hor] != " " and board_game[hor] == board_game[hor + 1] and board_game[hor + 1] == board_game[hor + 2]:
            return True
        # Vertical lines
        if board_game[ver] != " " and board_game[ver] == board_game[ver + 3] and board_game[ver + 3] == board_game[ver + 6]:
            return True 
        hor += 3
        ver += 1

    # Diagonal lines
    if board_game[dgl + 2] != " " and board_game[dgl + 2] == board_game[dgl +4] and board_game[dgl + 4] == board_game[dgl + 6]:
        return True
    if board_game[dgl] != " " and board_game[dgl] == board_game[dgl + 4] and board_game[dgl + 4] == board_game[dgl + 8]:
        return True


# Retorna o valro do proximo jogar que irá jogar
def getPayer(turn):
    return 1 if turn else 2

# Verifica se a casa está disponível
def is_empty_board(board):
    return True if board == " " else False

# Checa se o valor digita é menor que 9
def is_fase_less_9(fase, fase_max):
    return True if fase < fase_max else False

# Checa várias possibilidades
def check_list_all(game, fase, check, fase_max):
     return True if is_range_turn(game, check) and is_fase_less_9(fase, fase_max) and is_empty_board(game[int(check) - 1]) else False

# Verifica se está empatado
def is_tied(fase, fase_max, game):
    return True if fase >= fase_max and not win(game) else False

def is_range_turn(game, check):
    try:
        return game[int(check) - 1]
    except:
        print("Valor incorreto!!!")

# Desenha o tabuleiro
def draw(game):
    line1 = " | ".join(game[0:3])
    line2 = " | ".join(game[3:6])
    line3 = " | ".join(game[6:9])
    print()
    print(line1)
    print(line2)
    print(line3)

# Chamado o jogo
main()

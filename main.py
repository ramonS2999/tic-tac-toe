def main():
    game = [" "] * 9
    char = ["X", "O"]
    turn = True
    
    while True:
        draw(game)
        print(f"Turno: Jogador {str(getPayer(turn))}")
        check = input("Digite uma posição disponível oo intervalo de [1-9]: ")
        game[int(check) - 1] = char[getPayer(turn)- 1]
        if win(game):
            draw(game)
            print(f"O Jogador {getPayer(turn)} Venceu!")
            break
        turn = not turn

def win(game):
    # Hirizontal lines
    if game[0] != " " and game[0] == game[1] and game[1] == game[2]:
        return True
    if game[3] != " " and game[3] == game[4] and game[4] == game[5]:
        return True
    if game[6] != " " and game[6] == game[7] and game[7] == game[8]:
        return True
    # Vertical lines
    if game[0] != " " and game[0] == game[3] and game[3] == game[6]:
        return True
    if game[1] != " " and game[1] == game[4] and game[4] == game[7]:
        return True
    if game[2] != " " and game[2] == game[5] and game[5] == game[8]:
        return True
    # Diagonal lines
    if game[0] != " " and game[0] == game[4] and game[4] == game[8]:
        return True
    if game[2] != " " and game[2] == game[4] and game[4] == game[6]:
        return True

def getPayer(turn):
    if turn:
        return 1
    else:
        return 2

def draw(game):
    line1 = " | ".join(game[0:3])
    line2 = " | ".join(game[3:6])
    line3 = " | ".join(game[6:9])
    print(line1)
    print(line2)
    print(line3)

main()

print("Bem-vindo ao Jogo: Pedra, Papel e Tesoura!")

#inicio do contador das vitorias/derrotas
win_gamer1 = 0
win_gamer2= 0
#estrutura de repetição, vai ser executado até um jogador ganhar 2 vezes ou der 3 empates
while True:
    for rodada in range(1, 4):
        print(f"Rodada {rodada}:")
        # lista de opções
        opcoes = ["Pedra", "Papel", "Tesoura"]
        print("Jogador 1, escolha uma das opções abaixo:")
        #enumerate(opcoes, start=1) serve para inumerar as opcoes de 1 até 3
        for i, opcao in enumerate(opcoes, start=1):
        # exibir as opções disponíveis para os jogadores escolherem
            print(f"{i} - {opcao}")
        jogador1 = int(input())
        print("Jogador 2, escolha uma das opções abaixo:")
        for i, opcao in enumerate(opcoes, start=1):
            print(f"{i} - {opcao}")
        jogador2 = int(input())
        # Verificação de quem venceu a rodada
        if jogador1 == jogador2:
            print("Rodada empatada!")
        #condições para vitoria do jogador 1
        elif (jogador1 == 1 and jogador2 == 3) or (jogador1 == 2 and jogador2 == 1) or (
                jogador1 == 3 and jogador2 == 2):
            print("Jogador 1 venceu a rodada!")
            win_gamer1 += 1
        else:
            print("Jogador 2 venceu a rodada!")
            win_gamer2 += 1
        # vendo se um dos jogadores já venceu 2 rodadas para dar o vencedor
        if win_gamer1 == 2:
            print("Jogador 1 venceu o jogo!")
            break
        elif win_gamer2 == 2:
            print("Jogador 2 venceu o jogo!")
            break
    #perguntando se o usuario deseja jogar o jogo denovo, caso digite qualquer outra str alem de "s", o jogo encerra
    resetjogo = input("Deseja jogar novamente? (s/n): ")
    if resetjogo.lower() != "s":
        break

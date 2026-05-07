import random

lista = ['papel', 'pedra', 'tesoura']
while True:
    jogador = (0)
    maquina = (0)
      jogador < 3 and maquina < 3:

     jogador = input("Escolha entre pedra, papel e tesoura: ").lower()
     maquina = random.choice(lista)
     print("a maquina jogou: ",(maquina))

    if jogador not in lista:
        print("Essa opção não existe, amigo.")

    elif jogador == maquina:
        print("deu empate :P")

    if (jogador == 'pedra' and maquina == 'pappel') or \
    

    #else:
     #   print("ponto pra maquina")
      #  maquina = maquina+1

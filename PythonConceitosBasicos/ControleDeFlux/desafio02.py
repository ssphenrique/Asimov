"""
Crie um programa que:
Escolhe um número secreto.
Pede por um chute do usuário.
Indica se o usuário acertou ou não.
Se não acertou, dá uma dica, dizendo se o número é mais ou mais baixo.
Repete isso até 3 vezes!

"""
import random
numero_secreto = random.randint(0,10)

for tentativa_num in range(3):
    tentativa = int(input(f"Tentativa {tentativa_num + 1} de 3: Escolha um número entre 1 e 10.\n"))

    if tentativa == numero_secreto:
        print("Você acertou")
        break
    elif tentativa > numero_secreto:
        print("O número é menor que o número escolhido")
    else:
        print("O número é maior que o número escolhido")

else:
    print("Você esgotou as suas três tentativas")
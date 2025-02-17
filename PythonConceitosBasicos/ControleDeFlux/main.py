"""
age = int(input("Digite sua idade: "))

if age < 18:
    print("Você tem menos de 18 anos")
elif age == 18:
    print("Você tem exatamento 18 anos")
else:
    print("Você tem mais de 18 anos")
"""

"""
print("----------Inicio----------")

resposta1 = input("Estou com fome?\nDigite s para sim\n")

if resposta1 ==  "s":
    resposta2 = input("Tenho comida em casa?\n")
    if resposta2 != "s":
        print("Ir ao mercado")
        print("Voltar para casa")
    print("Preparar uma refeição")
    print("Comer a comida")

print("----------FIM----------")

"""

#Para saber se as condições são verdadeiras 
estou_com_fome = input("Estou com fome? ") == "s"
tenho_comida = input("Tenho comida em casa? ") == "s"

#Verifica as condições, caso for verdadeira, segue criando novas mensagens, se não, FIM.
if estou_com_fome and not tenho_comida:
    print("Ir ao mercado")
    print("Voltar para casa")
    print("Preparar uma refeição")
    print("Comer a comida")

if estou_com_fome and tenho_comida:
    print("Preparar uma refeição")
    print("Comer a comida")

print("FIM")
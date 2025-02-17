"""
Desafio - crie um programa que:
Pede pelo seu nome e idade
Dá oi para você
Conta quantas letras seu nome possui
Fala quantos anos você terá daqui a 5 anos
"""

name = str(input("Qual o seu nome? "))
age = int(input("Quantos anos você tem? "))

print(f"Olá {name}")
print(f"Seu nome possui {len(name)} letras")
print(f"Daqui a 5 anos, você terá {age + 5}")
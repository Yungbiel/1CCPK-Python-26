# def boas_vindas(nome):
#     print(f"Olá , {nome}! Seja bem vindo!")
#
# nome_digitado = input("Digite seu nome: ")
# boas_vindas(nome_digitado)
#
# def  soma(num_a + num_b):
#     soma = num_a + num_b
#     return soma
#
# resultado_soma = soma(5, 3)
# print(resultado_soma)

#Exercío

import pygame

pygame.mixer.init()

pygame.mixer.music.load("musica.mp3")

pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue

#Execício 2

numero = int(input("Digite um número: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

#Exercício 3

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os dois números são iguais.")

#Exercício 4

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"Média: {media:.2f}")

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Em recuperação")
else:
    print("Reprovado")

#Exercício 5

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))

if A % B == 0 or B % A == 0:
    print("São Múltiplos")
else:
    print("Não são Múltiplos")

#Exercício 6

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print("Resultado:", resultado)

#Exercício 7

from datetime import datetime

ano_atual = datetime.now().year

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_atual - ano_nascimento

print(f"Idade: {idade} anos")

if idade < 16:
    print("Voto proibido")
elif 16 <= idade < 18 or idade >= 70:
    print("Voto opcional")
else:
    print("Voto obrigatório")

#Exercício 8

salario = float(input("Digite o salário do colaborador: R$ "))

if salario <= 280:
    percentual = 0.20
elif salario <= 700:
    percentual = 0.15
elif salario <= 1500:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario * percentual
novo_salario = salario + aumento

print(f"Salário antes do reajuste: R$ {salario:.2f}")
print(f"Percentual de aumento aplicado: {percentual * 100:.0f}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")

#Exercício 9

estado = int(input("Digite o código do estado (1 a 5): "))
peso_toneladas = float(input("Digite o peso da carga (em toneladas): "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

peso_kg = peso_toneladas * 1000

if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
elif 31 <= codigo_carga <= 40:
    preco_kg = 340
else:
    preco_kg = 0
    print("Código de carga inválido!")

preco_carga = peso_kg * preco_kg

if estado == 1:
    imposto = preco_carga * 0.35
elif estado == 2:
    imposto = preco_carga * 0.25
elif estado == 3:
    imposto = preco_carga * 0.15
elif estado == 4:
    imposto = preco_carga * 0.05
elif estado == 5:
    imposto = 0
else:
    imposto = 0
    print("Código de estado inválido!")

# Valor total
total = preco_carga + imposto

# Saída
print(f"Peso da carga em kg: {peso_kg:.2f} kg")
print(f"Preço da carga: R$ {preco_carga:.2f}")
print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Valor total transportado: R$ {total:.2f}")

#Exercício 10

A = float(input("Digite o lado A: "))
B = float(input("Digite o lado B: "))
C = float(input("Digite o lado C: "))

lados = sorted([A, B, C], reverse=True)
A, B, C = lados  # Agora A é o maior

if A >= B + C:
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == B**2 + C**2:
        print("TRIANGULO RETANGULO")
    elif A**2 > B**2 + C**2:
        print("TRIANGULO OBTUSANGULO")
    elif A**2 < B**2 + C**2:
        print("TRIANGULO ACUTANGULO")

    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or A == C or B == C:
        print("TRIANGULO ISOSCELES")

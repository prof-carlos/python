import os

os.system("cls || clear")

print("=== Solicitando dados === \n")
primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
subtacao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

print("=== Exibindo resultados === \n")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtacao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
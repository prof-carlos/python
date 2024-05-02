import os

os.system("cls || clear")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
media = soma / 2
produto = primeiroNumero * segundoNumero

if primeiroNumero > segundoNumero:
    maiorNumero = primeiroNumero
else: 
    maiorNumero = segundoNumero

if primeiroNumero < segundoNumero:
    menorNumero = primeiroNumero
else: 
    menorNumero = segundoNumero

print("\n=== Exibindo resultados ===")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundonúmero: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")

import os

os.system("cls || clear")

primeiroNumero = int(input("Digite o primeiro número: "))
segundoNumero = int(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
media = soma / 2
produto = primeiroNumero * segundoNumero

maiorNumero = max(primeiroNumero, segundoNumero)
menorNumero = min(primeiroNumero, segundoNumero)

print("\n=== Exibindo resultados ===")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundonúmero: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Média: {media}")
print(f"Produto: {produto}")
if primeiroNumero == segundoNumero:
    print("São iguais.")
else: 
    print(f"Maior número: {maiorNumero}")
    print(f"Menor número: {menorNumero}")

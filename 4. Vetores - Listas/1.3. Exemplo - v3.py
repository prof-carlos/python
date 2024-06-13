import os

os.system("cls || clear")

# Criando uma lista / vetor.
numeros = []

# Solicitando 3 notas para o usuário.
while True:
    numero = float(input("Digite um número: "))
    if numero == 0:
        break
    numeros.append(numero) 

maiorNumero = max(numeros)
menorNumero = min(numeros)

# Exibindo as notas para o usuário.
# ForEach
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

# Exibindo maior número e menor número.
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
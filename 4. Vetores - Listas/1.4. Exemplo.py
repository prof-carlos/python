import os

os.system("cls || clear")

# Criando constante
QUANTIDADE_NUMEROS = 6

# Criando uma lista / vetor.
numeros = []

pares = 0
impares = 0

# Solicitando 6 números para o usuário.
for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero) 

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo as notas para o usuário.
# ForEach
for i, numero in enumerate(numeros):
    print(f"{i+1}º número: {numero}")

# Exibindo maior número e menor número.
print(f"Qunatidade de números pares: {pares}")
print(f"Qunatidade de números ímpares: {impares}")
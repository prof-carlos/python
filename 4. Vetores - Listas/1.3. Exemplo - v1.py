import os

os.system("cls || clear")

# Criando uma constante
QUANTIDADE_NOTAS = 5

# Criando uma lista / vetor.
numeros = []

maiorNumero = 0
menorNumero = 9999

# Solicitando 3 notas para o usuário.
for i in range(QUANTIDADE_NOTAS):
    numero = float(input("Digite um número: "))
    numeros.append(numero) 

    if numero > maiorNumero:
        maiorNumero = numero

    if numero < menorNumero:
        menorNumero = numero

# Exibindo as notas para o usuário.
# ForEach
for numero in numeros:
    print(f"Número: {numero}")

# Exibindo maior número e menor número.
print(f"Maior número: {maiorNumero}")
print(f"Menor número: {menorNumero}")
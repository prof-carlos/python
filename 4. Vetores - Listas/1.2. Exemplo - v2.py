import os

os.system("cls || clear")

# Criando uma constante
QUANTIDADE_NOTAS = 3

# Criando uma lista / vetor.
notas = []

# Solicitando 3 notas para o usuário.
for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite uma nota: "))
    notas.append(nota) 

media = sum(notas) / QUANTIDADE_NOTAS

# Exibindo as notas para o usuário.
for i in range(QUANTIDADE_NOTAS):
    print(f"Nota: {notas[i]}")

# ForEach
for nota in notas:
    print(f"Nota: {nota}")

# Exibindo média.
print(f"Média: {media}")
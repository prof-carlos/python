import os

os.system("clear")

nota: float = -1

while (nota < 0 or nota > 10) :
    nota = float(input("Digite uma nota: "))

print(f"Nota informada: {nota}")
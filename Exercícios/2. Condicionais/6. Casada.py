import os
os.system("cls || clear")

print("\n=== Solicitando dados ===")
nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo (M ou F): ")
estadoCivil = input("Digite seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoDeCasamento = input("Digite o tempo de casada (em anos): ")

print("\n=== Exibindo resultado ===")
print(f"Nome: {nome}")

if sexo == "f":
    print(f"Sexo: Feminino")
else: 
    print(f"Sexo: masculino")

print(f"Estado civil: {estadoCivil}")

if sexo == "F" and estadoCivil == "Casada":
    print(f"Tempo de casada: {tempoDeCasamento}")





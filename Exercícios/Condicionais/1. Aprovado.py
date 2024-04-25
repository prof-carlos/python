import os

os.system("cls || clear")

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
primeiraNota = float(input("Digite a primeira nota: "))
segundaNota = float(input("Digite a segunda nota "))
terceiraNota = float(input("Digite a terceira nota: "))

media = (primeiraNota + segundaNota + terceiraNota) / 3

if media >= 7: 
    resultado = "Aprovado."
else:
    resultado = "Reprovado."

print("\n=== Exibindo resultados ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {primeiraNota}")
print(f"Segudna nota: {segundaNota}")
print(f"Terceira nota: {terceiraNota}")
print(f"Média: {media}")
print(f"Resultado: {resultado}")


print("=== FIM ===")
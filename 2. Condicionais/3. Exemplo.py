import os

os.system("cls || clear")

peso = float(input("Digite seu peso: "))

if peso < 40: 
    print("Magro.")
elif peso < 80:
    print("Nomal.")
else: 
    print("Sobrepeso.") 

print("=== FIM ===")
import os

os.system("cls || clear")

print("\n=== Solicitando dados ===")
pesoMorangos = float(input("Digite o peso de morangos (em Kg): "))
pesoMacas = float(input("Digite o peso de maçãs (em Kg): "))

if pesoMorangos < 5:
    precoMorango = 2.50
else :
    precoMorango = 2.20

if pesoMacas < 5:
    precoMaca = 1.80
else: 
    precoMaca = 1.50

pesoTotal = pesoMorangos + pesoMacas
subtotal = (precoMorango * pesoMorangos) + (precoMaca * pesoMacas)

if pesoTotal > 8 or subtotal > 25:
    desconto = subtotal * 0.10
else: 
    desconto = 0

totalPagar = subtotal - desconto

print("\n=== Exibindo resultados ===")
print(f"Peso de morangos (em Kg): {pesoMorangos}")
print(f"Peso de maçãs (em Kg): {pesoMacas}")
print(f"Soma dos pesos (em Kg): {pesoTotal}")
print(f"Subtotal: R$ {subtotal:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {totalPagar:.2f}")

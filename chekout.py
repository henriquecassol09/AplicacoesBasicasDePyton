valor = float(input("qual o valor total das compras? "))
cupom = input("digite o cupom caso você tenha ")

if cupom == "QUERO10":
    print("cupom aplicado")
    valor = valor - (valor * 0.10)


if valor >= 200:
    print("voce tem direito a frete gratis!")
else:
    valor = valor + 20

print(f"o valor a ser pago é {valor}")
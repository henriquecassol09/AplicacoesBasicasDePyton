contador = 0
ID = float(input("qual o codigo do produto escolhido? "))
qnt = float(input("quantos produtos você deseja comprar? "))
total = 0

if ID == 100:
    while contador < qnt:
        total = qnt * 1.20
        contador += 1      
    print(f"o valor a ser pago é {total:g}")

if ID == 101:
    while contador < qnt:
        total = qnt * 1.30
        contador += 1
    print(f"o valor a ser pago é {total:g}")

if ID == 102:
    while contador < qnt:
        total = qnt * 1.50
        contador += 1
    print(f"o valor a ser pago é {total:g}")

if ID == 103:
    while contador < qnt:
        total = qnt * 1.20
        contador += 1
    print(f"o valor a ser pago é {total:g}")

if ID == 104:
    while contador < qnt:
        total = qnt * 1.70
        contador += 1
    print(f"o valor a ser pago é {total:g}")

if ID == 105:
    while contador < qnt:
        total = qnt * 2.20
        contador += 1
    print(f"o valor a ser pago é {total:g}")

if ID == 106:
    while contador < qnt:
        total = qnt * 1.00
        contador += 1
    print(f"o valor a ser pago é {total:g}")
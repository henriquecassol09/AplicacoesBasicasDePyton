valor = float(input("qual o valor do produto antes da inflação? "))

if valor <= 50:
    reajuste = valor * 1.05
    print(f"o valor depois do reajuste é de {reajuste}")
elif valor > 50 and valor <= 100:
    reajuste = valor * 1.10
    print(f"o valor depois do reajuste é de {reajuste}")
else:
    reajuste = valor * 1.15
    print(f"o valor depois do reajuste é de {reajuste}")
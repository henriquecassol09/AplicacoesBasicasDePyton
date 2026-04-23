n1 = float (input("qual o primeiro numero? "))
n2 = float (input("qual o segundo numero? "))
operacao = int (input("para fazer a media entre os numeros digite 1, para a deferença dos numeros digite 2, para o produto dos numeros digite 3 e para a divição dos numeros digite 4 "))

if operacao == 1:
    r1 = (n1 + n2) / 2
    print(f"a media entre os numeros é {r1:g}")
elif operacao == 2:
    r1 = n1 - n2
    print(f"a diferença dos numeros é {r1:g}")
elif operacao == 3:
    r1 = n1 * n2
    print(f"a produto dos numeros é {r1:g}")
elif operacao == 4 and n2 != 0:
    r1 = n1 / n2
    print(f" a divisão dos numeros é {r1:g}")
else:
    print(f"você digitou um numero resultante de operação errada ou a operação é invalida mediante aos numeros")

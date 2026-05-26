numero1 = float(input("qual o primeiro numero?"))
numero2 = float(input("qual o segundo numero?"))
numero3 = float(input("qual o terceiro numero?"))

if numero1 > numero2 and numero1 > numero3:
    if  numero2 > numero3:
        print(numero3, numero2, numero1)
    else:
        print(numero2, numero3, numero1)
elif numero2 > numero1 and numero2 > numero3:
    if numero1 > numero3:
        print(numero3, numero1, numero2)
    else:
            print(numero1, numero3, numero2)
else:
    if numero1 > numero2:
        print(numero2, numero1, numero3)
    else:
            print(numero1, numero2, numero3)
altura = float(input("qual sua altura em centimetros? "))
peso = float(input("qual seu peso kilos? "))


if altura <= 120:
    if peso <= 60:
        print("Sua clasificação é A")
    elif peso > 60 and peso <= 90:
        print("Sua clasificação é D")
    else:
        print("Sua clasificação é G")
    
if altura > 120 and altura <= 170:
    if peso <= 60:
        print("Sua clasificação é B")
    elif peso > 60 and peso <= 90:
        print("Sua clasificação é E")
    else:
        print("Sua clasificação é H")

if altura > 170:
    if peso <= 60:
        print("Sua clasificação é C")
    elif peso > 60 and peso <= 90:
        print("Sua clasificação é F")
    else:
        print("Sua clasificação é I")

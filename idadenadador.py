idade = int (input("qual sua idade"))

if idade >= 18:
    print (f"você faz parte da categoria dos adultos")
else:
    if idade >= 14:
        print (f"você faz parte da categoria juvenil B")
    else:
        if idade >= 11:
            print (f"você faz parte da categoria juvenil A")
        else:
            if idade >= 8 :
                print(f"você faz parte da categoria infantil B")
            else:
                print (f"você faz parte da categoria infantil A")
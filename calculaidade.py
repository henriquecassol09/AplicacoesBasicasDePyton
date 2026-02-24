ano = float (input("em que ano você nasceu? "))
data = float (input("qual a data atual"))

idadeA  = data - ano
idadeM = idadeA * 30
idadeD = idadeA * 365

print(f"sua idade em anos é {idadeA:g}")
print(f"sua idade em meses é {idadeM:g}")
print(f"sua idade em dias é {idadeD:g}")

#henriquecassol 
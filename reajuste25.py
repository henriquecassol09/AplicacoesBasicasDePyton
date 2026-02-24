salario = float (input("qual seu salario atual? "))
valorreajuste = float (input("qual valor do seu reajuste? (sem o sinal de %)"))

porcentagem = (valorreajuste/100) + 1

reajuste = salario * porcentagem


print(f"seu salario depois do reajuste de é {reajuste:g}")

#henriquecassol

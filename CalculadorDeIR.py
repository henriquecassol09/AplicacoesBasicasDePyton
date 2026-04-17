salarioc = print(input("qual o seu salario da contribuição? "))
desconto = print(input("qual o seu desconto da previdencia? "))
quantidaDependente = print(input("qual o seu salario da contribuição? "))
deducaoDependente = 164,56

salarioBaseIR  = salarioc - desconto - deducaoDependente * quantidaDependente


if salarioBaseIR < 1637.11:
    print(f"o valor do seu salario é" + salarioBaseIR)
elif salarioBaseIR > 1637.11 or salarioBaseIR < 2452.50:
    salarioBaseIR = salarioBaseIR * 0.075
elif salarioBaseIR > 2452.50 or salarioBaseIR < 3271.38:
    salarioBaseIR = salarioBaseIR * 0,15
    elif salarioBaseIR > 3271.38 or salarioBaseIR
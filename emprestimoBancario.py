salario = float(input("Qual o seu salario? "))
emprestimo = float(input("Qual o valor do emprestimo desejado? "))
score = int(input("Qual o seu score de credito (de 0 a 1000)? "))

verificador = salario * 0.30

if emprestimo > verificador or score < 500:
    print("Empréstimo negado!")
else:
    print("Empréstimo aprovado com sucesso!")

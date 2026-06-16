print("Responda TODAS as opções abaixo com S para sim e N para não")

n3 = "N"
pontos = 0

n1 = input("Você esta sentindo falta de ar ou dor no peito? ")
n2 = input("Você esta com sintomas graves ou em uma escala de 0-10 você clasifica sua dor como 10? ")


if n1 == "S" or n1 == "s":
    pontos = pontos + 5


if n2 != "S" and n2 != "s":
    n3 = input("Em uma escala de 0-10 sua dor se encontra entre 7 e 9? ")
else:
    pontos = pontos + 5

if n3 == "S" or n3 == "s":
    pontos = pontos + 3

if pontos >= 8:
    print("Você tem atendimento de urgencia")
elif pontos >= 5:
    print("Você sera atendido logo apos os pacientes urgentes")
else:
    print("Seu caso não se enquadra como grave ou urgente por favor espere!")
    
nota1 = int (input("qual a nota do primeiro trimestre?"))
nota2 = int (input("qual a nota do primeiro trimestre?"))
nota3 = int (input("qual a nota do primeiro trimestre?"))
media = nota1 + nota2 + nota3 / 3

if media > 60:
  print (f"aprovado")
else:
  print (f"reprovado")
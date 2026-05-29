vendas = float(input("qual o valor em reais de vendas que você vendeu esse mes? "))

if vendas >= 100000:
    comicao = 700 + vendas * 0.16
    print(f"o valor da comição que você deve receber é de {comicao}")
elif vendas < 100000 and vendas >= 80000:
    comicao = 650 + vendas * 0.14
    print(f"o valor da comição que você deve receber é de {comicao}")
elif vendas < 80000 and vendas >= 60000:
    comicao = 600 + vendas * 0.14
    print(f"o valor da comição que você deve receber é de {comicao}")
elif vendas < 60000 and vendas >= 40000:
    comicao = 550 + vendas * 0.14
    print(f"o valor da comição que você deve receber é de {comicao}")
elif vendas < 40000 and vendas >= 20000:
    comicao = 500 + vendas * 0.14
    print(f"o valor da comição que você deve receber é de {comicao}")
elif vendas <= 20000:
    comicao = 400 + vendas * 0.14
    print(f"o valor da comição que você deve receber é de {comicao}")
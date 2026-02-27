preco = float (input("qual o preço normal da etiqueta do produto desejado "))
text1 = int (input("Para pagamento á vista em dinheiro ou cheque, digite 1. Para pagamentos á vista no cartão de crédito, digite 2. Para pagamentos duas vezes, digite 3. Para pagamentos em ate tres vezes digite 4. "))

if text1 == 1:
    var1 = preco - (preco * 0.10)
    print(f"o valor a ser pago é {var1:g}")
elif text1 == 2:
        var2 = preco -(preco * 0.15)
        print(f"o preço a ser pago é {var2:g}")
elif text1 == 3:
         var4 = preco
         print(f"o valor a ser pago é {var4:g}")
else: text1 == 4
var3 = preco * 1.10
print(input(f"o preço a ser pago é {var3:g}"))
    
 

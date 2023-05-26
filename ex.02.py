compra = float(input("Digite o valor da sua compra: "))
pres = int(input("Digite a quantidade de prestação: "))
result = compra / pres

if result > 500:
    print("Não consegue pagar!")
else:
    print("Consegue pagar")
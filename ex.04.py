n1= float(input("Digite um número decimais ou inteiros: "))
n2 = float(input("Digite o segundo: "))

op = str(input('Informe qual operação deseja:'
           '\n(A) Multiplicação'
           '\n(B) Divisão'
           '\n(C)Adição'
           '\n(D) Subtração'))
A = n1 * n2
B = n1 / n2
C = n1 + n2
D = n1 - n2

if op.upper() =="A":
    print("O resultado foi: ", A)

elif op.upper()  == "B":
    print("O resultado foi: ", B)

elif op.upper()  == "C":
    print("O resultado foi: ", C)

else:
    print("o resultado foi: ", D)
#nome = input("Qual seu nome? ")
#print("Prazer em te conhecer {:^20}!".format(nome))

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("\nA soma é {}, a multiplicação é {} e a divisão é {}\n".format(s, m, d))
print("A divisão inteira é {} e a potencia é {}".format(di,e ))

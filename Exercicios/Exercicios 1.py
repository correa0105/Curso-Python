'''#CRIE UM PROGRAMA QUE LEIA O O NUMERO INTEIRO E MOSTRE NA TELA SEU SUCESSOR E SEU ANTECESSOR.

n1 = int(input("Digite um valor que queira saber seu sucessor e seu antecessor: "))

ant = n1 - 1
suc = n1 + 1

print("Seu antecessor é: {} e seu sucessor é: {}".format(ant, suc))'''

'''#CRIE UM PROGRAMA QUE LEIA O NUMERO E MOSTRE SEU DOBRO SEU TRIPLO E SUA RAIZ QUADRADA.

n1 = int(input("Digite um valor que queira saber seu dobro, triplo e sua raiz quadrada: "))

dob = n1 * 2
trip = n1 * 3
raiz = n1**(1/2)

print("Seu doubro é: {}, seu triplo {} e sua raiz quadrada é: {}".format(dob, trip, raiz))'''

'''#CRIE UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNA, CALCULE E DE A MÉDIA.

n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua primeira nota: "))

media = (n1 + n2)/2

print("Sua média é: {}".format(media))'''

'''#CRIE UM PROGRAMA QUE LEIA O VALOR EM METROS E CONVERTA PARA CENTIMETRO E MILIMETROS

n1 = int(input("Digite uma medida em metros que vou converter para centimetros e milimetros: "))

mm = n1 * 1000
cm = n1 * 100

print("{} metros em centimetros é: {} e em milimetros é {}".format(n1, cm, mm))'''

'''#CRIE UM PROGRAMA QUE LEIA O O NUMERO INTEIRO E MOSTRE SUA TABUADA.

n1 = int(input("Digite um numero que exibirei sua tabuada: "))

print("-"*13)
print("{:<2} x {:2} = {}".format(n1, 1, n1*1))
print("{:<2} x {:2} = {}".format(n1, 2, n1*2))
print("{:<2} x {:2} = {}".format(n1, 3, n1*3))
print("{:<2} x {:2} = {}".format(n1, 4, n1*4))
print("{:<2} x {:2} = {}".format(n1, 5, n1*5))
print("{:<2} x {:2} = {}".format(n1, 6, n1*6))
print("{:<2} x {:2} = {}".format(n1, 7, n1*7))
print("{:<2} x {:2} = {}".format(n1, 8, n1*8))
print("{:<2} x {:2} = {}".format(n1, 9, n1*9))
print("{:<2} x {:1} = {}".format(n1, 10, n1*10))
print("-"*12)'''

'''#CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO A PESSOA TEM NA CARTEIRA E DIGA QUANTO DOLAR ELA PODE COMPRAR, VALOR DO DOLAR R$5,21

n1 = int(input("Converta o seu dinheiro para U$: "))

dol = n1 / 5.21

print("R${:.2f} em dolar é: U${:.2f}".format(n1, dol))'''

'''#CRIE UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS E CALCULE SUA AREA E A QUANTIDADADE DE TINTA NECESSARIA PARA PINTA-LA,
#SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2m²

larg = float(input("Largura da parede em metros: "))
alt = float(input("Altura da parede em metros: "))

area = larg * alt
qtdTinta = area / 2

print("A area da sua parede é {}m², e para pintala voce vai precisar de {} Litros de tinta".format(area, qtdTinta))'''

'''#CRIE UM PROGRAMA QUE LEIA O PREÇO DO PRODUTO E MOSTRE SEU NOVO PREÇO COM 5% DE DESCONTO.
#CRIE UM PROGRAMA QUE LEIA O SALARIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALARIO, COM 15% DE AUMENTO.

salario = float(input("Informe seu salario: "))
aumento = float(input("Informe o percentuaç de aumento: "))

novoSalario = salario + (salario * 15 / 100)

print("Seu novo salario é {:.2f}".format(novoSalario))'''

'''#CRIE UM PROGRAMA QUE CONVERTA ºC EM ºF

temp = float(input("Informe a temperatura em ºC: "))

tempF = ((1.8 * temp) + 32)

print("{:.1f}ºC correspondem a {:.1f}ºF".format(temp, tempF))'''

#CRIE UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS QUE ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR,
#SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0,15 POR KM RODADO.

km = float(input("Quantos KM voce percorreu com o veiculo? "))
dias = float(input("Quantis Dias voce alugou o carro? "))

pagar = (km * 0.15) + (dias * 60)

print("Voce deve pagar R${:.2f} pelo carro!".format(pagar))
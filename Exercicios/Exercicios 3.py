'''#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE, O NOME COM TODAS LETRAS MAIUSCULAS, MINUSCULAS,
#QUANTAS LETRAS TEM SEM CONTAR OS ESPAÇOS, E TAMBEM QUAL O PRIMEIRO NOME

nome = str(input("Digite seu nome completo: ")).strip() #strip para remover espaços das pontas

print("Seu nome em maiúsculas é {}".format(nome.upper()))
print("Seu nome em minúsculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(" ")))
separaNome = nome.split()
print("Seu primeiro nome é: {}".format(separaNome[0]))'''

'''#CRIE UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA E MOSTRE, UNIDADE, DEZENA, CENTENA E MILHAR

num = int(input("Digite um numero do 0 ao 9999: "))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print("Analisando o numero: {}".format(num))
print("Unidade: {}".format(unidade))
print("Dezena: {}".format(dezena))
print("Centena: {}".format(centena))
print("Milhar: {}".format(milhar))'''

'''#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE E DIGA SE ELA COMEÇA OU NÃO COM A PALAVRA "SANTO"

cidade = str(input("Digite o nome de uma cidade: ")).upper().strip().split() #DEIXA TUDO EM MAISCULA, REMOVE OS ESPAÇOS, SEPARA AS PALAVRAS EM BLOCOS

print("A sua cidade começa com Santo? {}".format("SANTO" in cidade[0]))'''

'''#CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E DIGA SE ELA TEM "SILVA" NO NOME

nome = str(input("Digite seu nome completo: ")).upper()

print("O seu nome tem Silva? {}".format("SILVA" in nome))'''

'''#CRIE UM PROGRAMA QUE LEIA UMA FRASE E MOSTRE: QUANTAS VEZES APARECE A LETRA "A", EM QUAL POSIÇÃO ELA PARECE A PRIMEIRA VEZ, EM QUAL POSIÇÃO ELA APARECE A ULTIMA VEZ

frase = str(input("Digite uma frase: ")).upper().strip()

print("A sua frase aparece a letra ""A"" {} vezes".format(frase.count("A")))
print("A letra ""A"" aparece a primeira vez na posição: {}".format(frase.find("A")+1))
print("A letra ""A"" aparece pela ultima vez na posição: {}".format(frase.rfind("A")+1))'''

'''#CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE O PRIMEIRO E O ULTIMO NOME DIGITADO.

nome = str(input("Digite seu nome completo: ")).strip().split()

contarNomes = len(nome)

print("Seu primeiro nome é: {}".format(nome[0]))
print("Seu ultimo nome é: {}".format(nome[contarNomes-1]))'''



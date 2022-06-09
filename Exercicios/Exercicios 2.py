import math
import random
import pygame

'''#CRIE UM PROGRAMA QUE LEIA UM NUMERO REAL QUALQUER, E MOSTRE SUA PARTE INTEIRA

num = float(input("Digite um valor real, e vou mostrar sua parte inteira: "))

nInteiro = math.trunc(num)

print("O numero {} inteiro fica: {}".format(num, nInteiro))'''

'''#CRIE UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRIANGULO RETANGULO E MOSTRE O COMPRIMENTO DE SUA HIPOTENUSA

cOposto = float(input("Informe o cateto Oposto: "))
cAdjacente = float(input("Informe o cateto Adjacente: "))

hipotenusa = math.hypot(cOposto, cAdjacente)
#hipotenusa = (cOposto ** 2 + cAdjacente ** 2) ** 0.5

print("A hipotenusa vai medir {:.2f}".format(hipotenusa))'''

'''#FAÇA UM PROGRMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DE SENO, COSSENO E TANGENTE DESSE ANGULO

angulo = float(input("Informe o angulo: "))

seno = math.sin(math.radians(angulo)) #FOI USADO O METODO PARA SEN, COS, TANG, POREM TEVE QUE CONVERTER PARA RADIANOS ANTES, POIS ESTAMOS FALANDO DE GRAU
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))

print("O Seno de {} é: {:.2f}".format(angulo, seno))
print("O Cosseno de {} é: {:.2f}".format(angulo, coss))
print("A Tangente de {} é: {:.2f}".format(angulo, tang))'''

'''#UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO, FAÇA UM PROGRAMA QUE LEIA O NOME DOS 4 ALUNOS E SORTEIO O NOME ESCOLHIDO

alu1 = str(input("Digite o nome do primeiro aluno: "))
alu2 = str(input("Digite o nome do segundo aluno: "))
alu3 = str(input("Digite o nome do terceiro aluno: "))
alu4 = str(input("Digite o nome do quarto aluno: "))

listaAluno = [alu1, alu2, alu3, alu4]

print("O aluno sorteado foi o:", random.choice(listaAluno))'''

'''#O MESMO PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHO DE ALUNOS, FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA

alu1 = str(input("Digite o nome do primeiro aluno: "))
alu2 = str(input("Digite o nome do segundo aluno: "))
alu3 = str(input("Digite o nome do terceiro aluno: "))
alu4 = str(input("Digite o nome do quarto aluno: "))

listaAluno = [alu1, alu2, alu3, alu4] #DEFINIR A LISTA
random.shuffle(listaAluno) #EMBARALHAR A LISTA

print("A ordem de apresentação é: ")
print(listaAluno)'''

'''#FAÇA UM PROGRAMA QUE ABRE E REPRODUZA UM ARQUIVO MP3

pygame.mixer.init() #AGUARDANDO UMA MUSICA PARA INICIAR
pygame.init() #INICIANDO A BIBLIOTECA DO PYGAME QUE É UMA BIBLIOTECA COM DIVERSAS FUNCIONALIDADES, VAMOS ULTILIZAR O MIXER PARA TOCAR MUSICA
pygame.mixer.music.load("outravida.mp3") #CARREGOU
pygame.mixer.music.play() #INICIOU A MUSICA
pygame.event.wait() #SÓ VAI FECHAR O PROGRAMA QUANDO A MUSICA ACABAR'''
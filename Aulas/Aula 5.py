#MANIPULANDO STRING

frase = "Aprendendo python por conta própria"

caracterUnico = frase[7]
caracterRange = frase[7:18]
caracterRangePulando = frase[7:18:2]
caracterRangeAté = frase[15:]
contarMicroEspaços = len(frase)
contarCaracter = frase.count("o")
encontrarParte = frase.find("thon")
temODado = "Aprendendo" in frase
substituirPalavra = frase.replace("conta","siri cascudo")
maiscula = frase.upper()
minuscula = frase.lower()
iniciaMaiuscula = frase.capitalize()
primeiraMaiuscula = frase.title()
removerEspaçosInuteis = frase.strip() #Tambem é possivel rstrip para remover os ultimos espaços ou lstrip para tirar os primeiros
dividirPalavrasEmStringNova = frase.split() #Separar cada palavra da frase em blocos separadas
juntarStringSeparadas = "-".join(frase) #Junta as letras ou espaços de string com o dado desejado no caso utilizei -

print("Valor encontrado:",caracterUnico)
print("Valor encontrado:",caracterRange)
print("Valor encontrado:",caracterRangePulando)
print("Valor encontrado:",caracterRangeAté)
print("Valor encontrado:",contarMicroEspaços)
print("Valor encontrado:",contarCaracter)
print("Valor encontrado:",encontrarParte)
print("Valor encontrado:",temODado)
print("Valor encontrado:",substituirPalavra)
print("Valor encontrado:",maiscula)
print("Valor encontrado:",minuscula)
print("Valor encontrado:",iniciaMaiuscula)
print("Valor encontrado:",primeiraMaiuscula)
print("Valor encontrado:",removerEspaçosInuteis)
print("Valor encontrado:",juntarStringSeparadas)





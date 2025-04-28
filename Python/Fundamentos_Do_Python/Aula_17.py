#Formatando string.

curso = "pYtHon"

print(curso.upper()) #Converte a string para "MAIUSCULO"

print(curso.lower()) #Converte a string para "minusculo"

print(curso.title()) #Deixa apenas a primeira letra como "MAISCULA"

#####################################################################################
#Removendo espacos em branco.

curso = "      Python"

print(curso.strip() + ".") #Remove os espaco a esquerda e a direita nao no meio da string

print(curso.lstrip() + ".") #Remove os espaco a esquerda da string

print(curso.rstrip() + ".") #Remove os espaco a direita da string 

#####################################################################################
#Juncao e centralizacao.

curso = "Python"

print(curso.center(10,"#")) #Centraliza a string defini numero maximo de caracteres e qual caractere sera usado para preencher o espaco em branco.
print(curso.center(10)) #Centraliza a string e mantem os espacos em branco.
print(".".join(curso)) #Perminte separar cada caractere da stringo por um caracterer que vc definir.
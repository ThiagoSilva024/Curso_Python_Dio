#Tupla: Armazena valores imutaveis

frutas = ("laranja", "pera", "uva",) 
#Uma virgula no final indentificau que e uma tupla.

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

#Acessando tupla:
#print(frutas[0]) #Retorna maca

tupla = ("p", "y", "t", "h", "o", "n",)
print(tupla[2:0]) #Retorna ("t", "h", "o", "n")
print(tupla[:2])  #Retorna ("p", "y")
print(tupla[1:3]) #Retorna ("y", "t")
print(tupla[0:3:2]) #Retorna ("p", "t")
print(tupla[::]) #Retorna ("p", "y", "t", "h", "o", "n")
print(tupla[::-1]) #Retorna ("n", "o", "h", "t", "y", "p")

for letra in tupla:
    print(letra,end="") #Percorre elemento por elemento

for indice, letra in enumerate(tupla):
    print(f"Indice da tupla{letra}:{indice}")

#Contar elementos dentro de uma tupla usando ().count:
linguagem = ("python", "js", "c", "java", "c#")

linguagem.index("java") # 3
linguagem.index("python") # 0
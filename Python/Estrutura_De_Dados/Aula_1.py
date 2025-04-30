""" #Listas
 
frutas = ["Laranja", "Maca", "Uva"]
print(frutas)

frutas = [] 
print(frutas)

letras = list("Python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "Sao Paulo", True]
print(carro)
 """


#Acesso direto.

""" frutas = ["Laranja", "Maca", "Uva"]
print(frutas[-1])
print(frutas[-3]) """

#Matrix Bidirecional

""" matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0]) #Exibe toda a linha
print(matriz[1][1]) #Acessa a linha ["b", 3, 4] e exibe o numero 3.
print(matriz[0][-1]) #Acessa a linha [1, "a", 2] e exibe o numero 4.
print(matriz[-1][-1]) #Acessa a linha [6, 5, "c"] e exibe o caracter 'c'. """

#Fatiamento

""" lista = ["p","y","t","h","o","n"]

print(lista[2:]) #Retorna ['t', 'h', 'o', 'n']
print(lista[:2]) #Retorna ['p', 'y']
print(lista[1:3]) #Retorna ['y', 't']
print(lista[0:3:2]) #Retorna ['p', 't']
print(lista[::]) #Retorna um copia da string['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1]) #Retorna ['n', 'o', 'h', 't', 'y', 'p'] """

#Acessar lista usando for

""" carros = ["gol", "celta", "palio"]
for carro in carros:
    print(carro)

#Funcao enumarate
for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}") 


for indice, carro in enumerate(carros):
    print(f"{indice} : {carro}")
 """

#Comprensao de listas

#Fitro versao 1 cria um lista com os numeros pares
numeros = [1, 30, 21, 2, 9, 65, 34]
""" 
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print("Numeros Pares".title)
for mostra in pares:
    print(mostra, end=" ") """

#Filtro versao 2 
""" pares = [numero for numero in numeros if numero % 2 == 0]

print("numeros pares".title().center(30,"="))

string = [str(s) for s in pares]

print("-".join(string)) """

#Modificando valores versao 1:
""" quandrado = []

for numero in numeros:
    quandrado.append(numero ** 2)

string_quadrado = [str(aux) for aux in quandrado]

print("-".join(string_quadrado)) """

#Modificando valores versao 2:
quadrado = [numero ** 2 for numero in numeros]
string = [str(aux) for aux in quadrado]

print("-".join(string))
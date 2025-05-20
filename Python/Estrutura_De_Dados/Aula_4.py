#Etapa 1
#Conjuntos: Uma colecao de objetos que possui elementos
#unicos.
#set([lista]): Elimina registros duplicados, nao garante
#ordem.

numeros = set([1, 2, 3, 1, 3, 4])
print(numeros)

letras = set("abacaxi")
print(letras)

palavras = set(("palio", "gol", "celta", "palio"))
print(letras)

linguagem = {"pytohn", "java", "pytohn"}
print(linguagem)

#Acessando os dados: Para isso e preciso converter
#o set para uma lista

numeros = {1, 2, 3, 2}

numero = list(numeros) #Transforma em lista
print(numero[0])

carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

#Funcao Enumarat

for indice, carro in enumerate(carro):
    print(indice)

#Etapa 2
#Metodos da classe set
#{}.union

conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) #Retorno {1,2,3,4}

#{}.intersection
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) #Retorna {2, 3}

#{}.difference
conjunto_e = {1, 2, 3}
conjunto_f = {2, 3, 4}

conjunto_e.difference(conjunto_f) #Retorna {1}
conjunto_f.difference(conjunto_e) #Retorna {4}

#{}.symmetric_difference
conjunto_g = {1, 2, 3}
conjunto_h = {2, 3, 4}

conjunto_g.symmetric_difference(conjunto_h) # Retorna {1, 4}

#{}issubset: Todos os elementos do 
#conjunto_i pertence ao conjunto_j
conjunto_i = {1, 2, 3}
conjunto_j = {4, 1, 2, 5, 6, 3}

conjunto_i.issubset(conjunto_j) #Retorna True
conjunto_j.issubset(conjunto_i) #Retorna False

#{}.issuperset: Todos os elementos do
#conjunto_k nao pertencem ao conjunto_l
conjunto_k = {1, 2, 3}
conjunto_l = {4, 1, 2, 5, 6, 3}

conjunto_k.issuperset(conjunto_l) #Retorna False
conjunto_l.issuperset(conjunto_k) #Retorna True

#{}.isdisjoint: Conjunto disjunto
#todos os elemntos de um conjunto nao estao no outro
conjunto_m = {1, 2, 3, 4, 5}
conjunto_n = {6, 7, 8, 9}
conjunto_o = {1, 0}

conjunto_m.isdisjoint(conjunto_n) #Retorna True
conjunto_n.isdisjoint(conjunto_o) #Retorna True
conjunto_o.isdisjoint(conjunto_m) #Retorna False

#{}.add: Passa um elemento e caso ele nao exista no
#conjunto ele e adicionado
sorteio = {1, 23}

sorteio.add(25) #Retorna {1, 23, 25}
sorteio.add(42) #Retorna {1, 23, 25, 42}
sorteio.add(25) #Retorna {1, 23, 25, 42} nao add pois ja
#existe o valor

#{}.clear: Limpa o set(conjunto)
sorteio = {1, 23}
 
sorteio #{1, 23}
sorteio.clear()
sorteio #{NULL}

#{}.copy: Gera um copia do set
sorteio = {1 ,23}

sorteio #{1, 23}
sorteio.copy()
sorteio #{1, 23}

#{}.discard: Descarta um valor
#nao retorna erro caso nao encontro o valor
numeros = {1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.discard(1)
numeros.discard(45) #Sera ignorado valor nao existe
numeros #{2, 3, 4, 5, 6, 7, 8, 9, 0}

#{}.pop: Remove valores, quanto mais .pop tiver
#mais valores seram removidos
numeros = {1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros #{1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.pop() #Removel {0}
numeros.pop() #Removel {1}
numeros #{2, 3, 4, 5, 6, 7, 8, 9}

#{}.remove: 
#retorna erro caso nao encontro o valor
numeros = {1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros #{1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}
numeros.remove(0) #Removel {0}
numeros #{1, 2, 3, 4, 5, 6, 7, 8, 9}

#{}.lne: Retona o tamanho do conjunto
numeros = {1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}

len(numeros) #Retorna 10

#in: Verifique se um objeto esta dentro de um conjunto
numeros = {1 ,2, 3, 4, 5, 6, 7, 8, 9, 0}

1 in numeros #True
10 in numeros #False

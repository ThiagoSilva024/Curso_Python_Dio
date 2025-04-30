# Metodos Da classe list
#Metodo [].append("valores") Adiciona valores de uma lista a uma nova lista

listas = []

listas.append(1)
listas.append("Python")
listas.append([1,2,3,4,5,6,7,8,9,10])
 
string = [str(aux) for aux in listas]
print(" - ".join(string)) 

#Metodo [].clear() Ultilizado para limpar a lista

print(listas)

listas.clear()

print(listas) 

#Método [].copy() cria uma cópia (nova instância) da lista,
# permitindo usá-la em outra parte do código sem interferir na lista original.

print(listas)
nova_lista = listas.copy()
print(id(listas), id(nova_lista))

print()

nova_lista[0] = "Thiago"
print(nova_lista)
print(listas) 

#Metodo [].count("objeto") possibilita contar quantas vezes um determinado oobjeto 
#aparece um um lista.

cores = ["vermelho", "azul", "verde", "azul"]
contador = cores.count("azul")

print(contador) 

#Método [].extend() permite adicionar todos os elementos de uma lista dentro de outra,
# unindo os conteúdos em uma única lista.

linguagem = ["python", "js", "c", "java", "c#"]

print(linguagem)
linguagem.extend(["java", 'c#'])
print(linguagem) 

#Método [].index(valor) retorna o índice (posição) da 
# primeira ocorrência do valor em uma lista.
# Se o valor não existir na lista, ocorre um erro.

print(linguagem.index("c")) 

#Método [].pop() remove e retorna o último item da lista.
# Também pode remover um item de um índice específico: [].pop(indice)
print(linguagem)

print(linguagem.pop())
print(linguagem.pop(0))

print(linguagem) 

#Método [].remove(valor) remove a primeira ocorrência do valor especificado na lista.
# Se o valor não estiver presente, ele gera um erro.

print(linguagem)
linguagem.remove("c")
print(linguagem) 

#Método [].reverse() inverte a ordem dos elementos da lista original, modificando-a 
# diretamente.

print(linguagem)
linguagem.reverse()
print(linguagem) 

# O método [].sort() ordena os elementos da lista **no próprio local** 
# (modifica a lista original).
# Por padrão, ele ordena em ordem crescente.
# Para ordem decrescente, use o argumento reverse=True.

print(f"\nLinguagens Desordenados:\n{linguagem}")
linguagem.sort()

print("=" * 40)

print(f"\nLinguagem Ordenados em ordem crescente:\n{linguagem}")

print("=" * 40)

print(f"\nLinguagem Ordenados em ordem crescente:\n{linguagem}")

print("=" * 40)

linguagem.sort(reverse=True)
print(f"\nLinguagem Ordenados em ordem decrescente:\n{linguagem}")

print("=" * 40)

linguagem.sort(key=lambda x: len(x))
print(f"\nOrdena as linguagem pelo numero de caracteres(Crescente):\n{linguagem}")

print("=" * 40)

linguagem.sort(key=lambda x: len(x), reverse=True)
print(f"\nOrdena as linguagem pelo numero de caracteres(Decrescente):\n{linguagem}")

print("=" * 40,"\n") 

# A função len() retorna a quantidade de elementos em uma lista 
# (ou em outra estrutura iterável).

print(len(linguagem)) 

## A função sorted(iterável) retorna uma nova lista com os elementos ordenados.
# Por padrão, a ordenação é crescente.
# Use reverse=True para ordem decrescente.

sorted(linguagem, key=lambda x: len(x))
print(linguagem)

print("=" * 40)

sorted(linguagem, key=lambda x: len(x), reverse=True)
print(linguagem)

print("=" * 40)

print(sorted(linguagem))
print("=" * 40)
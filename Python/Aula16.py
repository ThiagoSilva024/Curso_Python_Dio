  #Estrutura De Repeticao
a = int(input("Entre com um numero: "))

a += 1
print(f"Resultado: {a}")

a -= 1
print(f"Resultado: {a}")
 

 #Usando for
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

#Usando interavel. for/else, nao e comum de usar
texto = input("Digite um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Executa no filna do laco")
 
#Usando built-in range
for numero in range(0, 11):
    print(numero, end = " ")
print()
for numero in range(0, 51, 5):
    print(numero, end = " ")

#Usando while
opcao = -1

while opcao != 0:
    print("-" * 20,"\n1- Sacar.\n2- Extrato.\n0- Sair.\n", "-" * 20)

    opcao = int(input("Digite sua opcao: "))
    print( "-" * 20)

    if opcao == 1:
        print("\nSacando...\n")
    elif opcao == 2:
        print("\nExibindo o extrato ...\n")
else:
    print("\nObrigado por usar nosso sistema bancario, ate mais") 

 
opcao = 0

while opcao % 2 != 1:
    opcao = int(input("Informe um numero: "))
    
    if opcao % 2 == 0:
        print(f"Numero {opcao} e par")

else:
    print("O numero e impar") 


while True:
    numero = int(input("Informe um numero: "))

    if numero == 10:
        break
    
    print(numero) 

for numero in range(10000000):
    if numero == 4173829:
        break        

    print(numero) 

for numero in range(20):
    if numero == 12:
        continue
    
    print(numero, end = " ")


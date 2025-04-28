 # Neste desafio, voce deve escrever uma solucao
#que receba um numero inteiro como entrada e determine se ele e PAR ou impar.
#Dessa forma, a solucao deve retornar uma string indicando Par se o numero
#for PAR e IMPAR se o numero for IMPAR.

 # Solicita ao usuário um número inteiro
numero = int(input("Informe um valor:"))
#TODO: Verifique se o número é par ou ímpar e imprima o resultado:
if numero % 2 == 0:
  print("Par")
else:
  print("Ímpar ")

"""
#Versao com algumas melhorias
import os

while True:
    print("=" * 10, "VERIFICADOR DE PAR IMPAR", "=" * 10)
    
    num = int(input("Informe um numero: "))
    os.system("cls")
    
    if (num % 2) == 0:
        print("=" * 5,f"O valor informado {num} e PAR","=" * 5)
        print("\n")
    
    else:
        print("=" * 5,f"O valor informado {num} e IMPAR","=" * 5)
        print("\n")
    
    op = input("Deseja continuar: ")
    os.system("cls")
    
    if op == "n":
        print("\n\nOBRIGADO POR USAR NOSSO SISTEMA! ;)\n\n")
        break
    elif op == "s":
        continue
    else:
        print("Comando invalido! Retornando ao menu...")
        input("Precione ENTER para continuar...")
        
        os.system("cls")
        
 """
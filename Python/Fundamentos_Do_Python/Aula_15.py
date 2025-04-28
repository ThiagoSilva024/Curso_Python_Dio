 #Estruturas Condicionais
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Digite sua idade: "))
print("-" * 30)

#Usando if.
if idade < MAIOR_IDADE:
    print("\nNao possui idade minima para tirar CNH!\n")
    print(f"Idade atual: {idade} anos Idade minima: {MAIOR_IDADE} anos\n")
if idade >= MAIOR_IDADE: 
    print("\nPossui idade para tirar CNH!\n")
    print(f"Idade atual: {idade}\n")
print("-" * 30)

#Usando if, else. 
if idade < MAIOR_IDADE:
    print("\nNao possui idade minima para tirar CNH!\n")
    print(f"Idade atual: {idade} anos Idade minima: {MAIOR_IDADE} anos\n")
else:
    print("\nPossui idade para tirar CNH!\n")
    print(f"Idade atual: {idade}\n")
print("-" * 30)

#Usando if, elif e else.
if idade >= MAIOR_IDADE:
    print("\nNao possui idade minima para tirar CNH!\n")
    print(f"Idade atual: {idade} anos Idade minima: {MAIOR_IDADE} anos\n")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas nao pode fazer aulas praticas!")
else:
    print("\nPossui idade para tirar CNH!\n")
    print(f"Idade atual: {idade}\n")
print("-" * 30)

 #if aninhado: if dentro de if
saldo = 2000
saque = 1500
saque_especial = 450

print("-" * 10," TIPOS DE CONTAS ", "-" * 10)
print("1- Conta Normal")
print("2- Conta Universitaria")
print("3- Conta Especial")
print("-" * 10," TIPOS DE CONTAS ", "-" * 10)

tipo_conta = int(input("Informe o tipo da sua conta: "))

if tipo_conta == 1:
        if saldo >= saque:
            print("\nSaque realizado com sucesso!\n")
        elif saque <= (saldo + saque_especial):
            print("\nSaque realizado com o uso de cheque especial!\n")
        else: 
              print("Nao foi possivel realizar o saque, saldo insuficiente!")
elif tipo_conta == 2:
        if saldo >= saque:
             print("\nSaque realizado com sucesso!\n")
        else:
             print("\nSaldo insuficiente!\n")
elif tipo_conta == 3:
    print("\nConta especial selecionada!\n")
else:
      print("\nConta Invalida!\n")


#if ternario: Condicao em uma linha
saldo = 2000
saque = 2500
status = "Sucesso" if saldo >= saque else "Falha"

print(f"\n{status} ao realizar o saque!\n")
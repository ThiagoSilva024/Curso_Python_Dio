#Interpolacao de string

#Old style %

nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

print("Nome: %s \nIdade: %d" % (nome, idade))
print("-" * 20)
print("Nome: {} \nIdade: {}".format(nome, idade))
print("-" * 20)
print("Nome : {0} \nIdade: {1}".format(nome, idade)) #Ultilizando indices
print("-" * 20)
print("Nome: {nome} \nIdade:{idade}".format(nome = nome, idade = idade)) #Ultilizando nomeado
print("-" * 20)
print("Nome: {nome} \nIdade: {idade}".format(**dados))
print("-" * 20)
print(f"Nome:{nome} \nIdade:{idade} \nSaldo: {saldo:10.2f}")
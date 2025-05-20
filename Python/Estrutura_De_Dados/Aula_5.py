#Dicionarios: 
#Criando dicionario: Conjunto nao-ordenado de pares
#chaves:valor, uma chave valida deve ser imutavel
#os valores podem ser mutaveis

pessoa = {"nome:": "Guilherme", "idade:": 28} #Dicionario

pessoa = dict(nome="Guilherme", idade=28) #Declaracao equivalente

pessoa["telefone"] = "333-1234" #Adicionando uma nova chave

#Acessando os Dados: nome_dicionario["nome_chave"]

print(pessoa["nome"])
print(pessoa["idade"])
print(pessoa["telefone"])

#Sobre escrevendo valor:
pessoa["nome"] = "Thiago"
pessoa["idade"] = 24
pessoa["telefone"] = "(35)99982-1297"

print(pessoa)

#Estrutura aninhada: Uma estrutura dentro da outra
contatos = {
    "guilerme@gmail.com": {"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com": {"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com": {"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com": {"nome":"Melaine", "telefone":"3333-7766"},
}

contatos["giovanna@gmail.com"]["telefone"]
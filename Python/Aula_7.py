nome = input("Informe o seu nome:")
idade = input("Informe a sua idade:")

print(nome, idade)
print(nome, idade, end="...\n")
#Funcao "end='conteudo'" aplica um conteudo no final do print
print(nome, idade, sep=" # ") 
#Funcao "sep='conteudo'" aplica um conteudo entre as variavei do print
print(nome, idade, sep=" - ", end=".")
#E possivel usar os dois metodos juntos


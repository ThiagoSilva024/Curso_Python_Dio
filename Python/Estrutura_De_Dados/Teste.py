#Estrutura aninhada: Uma estrutura dentro da outra
contatos = {
    "guilerme@gmail.com": {"nome":"Guilherme", "telefone":"3333-2221"},
    "giovanna@gmail.com": {"nome":"Giovanna", "telefone":"3443-2121"},
    "chappie@gmail.com": {"nome":"Chappie", "telefone":"3344-9871"},
    "melaine@gmail.com": {"nome":"Melaine", "telefone":"3333-7766", "extra":{"a":1}},
}

print(contatos["giovanna@gmail.com"]["telefone"])
extra = contatos["melaine@gmail.com"]["extra"]["a"]
print(extra)

#Funciona mas nao e recomendado
for chave in contatos: 
    print(chave, contatos[chave])

for cahve, valor in contatos.items():
    print(chave, valor)

    
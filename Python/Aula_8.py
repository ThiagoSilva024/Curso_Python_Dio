produto_1 = 20
produto_2 = 10

print(f"ADICAO:-----------{produto_1 + produto_2}")
print(f"SUBTRACAO:--------{produto_1 - produto_2}")
print(f"MULTIPLICACAO:----{produto_1 * produto_2}")
print(f"DIVISAO:----------{produto_1 / produto_2}")
print(f"DIVISAO INTEIRA:-{produto_1 // produto_2}")
print(f"MODULO:-----------{produto_1 % produto_2}")



x = 10 + 5 * 4 #Sem precedencia
x = (10 + 5) * 4 #Usando precedencia
y = (10 / 2) + (25 * 2) - (2 ** 2) # Boas praticas: Separar operadores com parenteses
y = 10 / 2 + 25 * ((2 - 2) ** 2) 
print(x)

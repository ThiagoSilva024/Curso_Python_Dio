#Operadores Logicos
""" print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not(True and True))
print(not(True and False))
print(not(True or False))
print(not(True or True))
print(not(False or False)) """

saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(f"Resultado1: {exp}")

exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)

conta_com_saldo_suficiente = saldo >= saque and saque <= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

exp_3 = conta_com_saldo_suficiente or conta_especial_com_saldo_suficiente

print(f"Resultado2: {exp_3}")

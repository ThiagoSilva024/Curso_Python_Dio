#Escreva uma solucao que informe se um determinado ano e bissexto.
#Um ano e considerado bissexto se ele for divisivel por 4.
#No entanto, anos que sao divisiveis por 100 nao sao bissextos, a 
#menos que tambem sejam divisiveis por 400. Esta regra e usada para
#corrigir o calendario de modo que ele fique em conformidade com o 
#ano solar.

def verificador_ano_bissexto():
    ano = int(input())

    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print("BISSEXTO")
    else:
        print("NAO BISSEXTO")
        
verificador_ano_bissexto()
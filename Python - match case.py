# 16) Dado o dia da semana de 1 à 7, escreva na tela o correspondente por extenso
# (Domingo, Segunda-feira, ..., Sábado).

dia = int(input("Informe o dia da semana em números: "))

match(dia):
    case 1:
        print("Domingo")
    case 2:
        print("Segunda-Feira")
    case 3:
        print("Terça-Feira")
    case 4:
        print("Quarta-Feira")
    case 5:
        print("Quinta-Feira")
    case 6:
        print("Sexta-Feira")
    case 7:
        print("Sábado")
    case _:
        print("Dia Inválido")

# 15) Elabore um programa que leia um número inteiro entre 1 e 12 e
# imprima o mês correspondente. Caso seja digitado um valor fora desse
# intervalo, deverá ser exibida uma mensagem informando que não existe
# mês com esse número.

mes = int(input("Digite o número do mês: "))

match(mes):
    case 1:
        print("Janeiro")
    case 2:
        print("Fevereiro")
    case 3:
        print("Março")
    case 4:
        print("Abril")
    case 5:
        print("Maio")
    case 6:
        print("Junho")
    case 7:
        print("Julho")
    case 8:
        print("Agosto")
    case 9:
        print("Setembro")
    case 10:
        print("Outubro")
    case 11:
        print("Novembro")
    case 12:
        print("Dezembro")
    case _:
        print("Mês Inválido!")

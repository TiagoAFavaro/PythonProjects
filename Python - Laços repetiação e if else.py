valor = 1
contador = 0
maior = 0
menor = 0

while valor != 0:
    valor = int(input("Digite um valor: "))
    contador += 1
    if valor > 0:
        if contador == 1:
            menor = maior = valor
        else:
            if valor > maior:
                maior = valor
            if valor < menor:
                menor = valor
            
print("O maior valor é: ", maior)
print("O menor valor é: ", menor)

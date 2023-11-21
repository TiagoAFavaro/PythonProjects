#exercicio 4 lista 5

from datetime import date
ano_atual = date.today().year

joao = 1.45
maria = 1.57
ano = 2022

while joao < maria:
    joao += 0.23
    maria += 0.15
    ano = ano + 1
   
    
    print ("Altura joao", joao, ano)
    print ("Altura Maria", maria, ano)
   
    

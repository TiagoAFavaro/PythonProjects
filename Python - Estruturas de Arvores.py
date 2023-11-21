#Nome: Tiago Afonso Fávaro
#RA: 0762/14-3



verificacao = "Sim" 
print()

while (verificacao == "Sim"):
    print("Árvore Genealógica [Sequência: Pai | Mãe]")
    print("Nível 0 [Tiago e Primos parte de mãe]: Tiago, Mickael, Renato, Ramon, Rogério, Guilherme, Miguel, Gabriel, Aline, Alice, Fernando, Evelyn,Davi, Felipe ")
    print("Nível 0 [Tiago e Primos parte de pai]: Tiago, Rogério, Marcos, Flávio, Neusa, Michele, William, Vanessa, Priscila" ) 
    print()

    pais = str(input("Deseja pesquisar por qual parentesco ? [Pai | Mãe]  "))
    pais = pais.lower()
    pais = pais.capitalize() 
    pais = pais.replace("Mae", "Mãe")
    print()

    while pais != 'Pai' or 'Mãe':
        if pais == "Pai": 
            break 
        elif pais == "Mãe": 
            break 
        else: 
            print("Escolha entre Pai ou Mãe") 
            print()
            pais = str(input("Deseja pesquisar por qual parentesco ? [Pai | Mãe] "))
            pais = pais.lower()
            pais = pais.capitalize() 
            pais = pais.replace("Mae", "Mãe")
            print()

    if (pais == "Pai"): 
        print("Nível 1 [Pai e Tios]: Antonio, Aristeu, Luiz")
        print("Nível 2 [Avôs]: Antônio e Maria")
        print("Nível 3 [Bisavôs]: Luigi e América")
    elif (pais == "Mãe"): 
        print("Nível 1 [Mãe e Tios]: Maria, Milena, Marlene, Maura, Marleide, Clovis, Gil, Geraldo, João, Valcir, Lúcio  ")
        print("Nível 2 [Avôs]: Autimio e Deolinda")
        print("Nível 3 [Bisavôs]: Sem Informações")

    print()
    verificacao = str(input("Deseja realizar outra pesquisa ? [Sim | Não] "))
    if (verificacao == "Não"):
        print ("FIM")
    verificacao = verificacao.lower() 
    verificacao = verificacao.capitalize()
    print()


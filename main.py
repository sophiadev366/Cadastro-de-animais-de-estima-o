from animal import Animal, Cachorro, Gato

    
while True:
        print("""
        #========📚 Menu Principal 📚========#
        1 - Adicionar animal 
        2 - Remover animal
        3 - Buscar animal
        4 - Exibir animais
        5 - Adicionar dono
        6 - Remover dono
        7 - Buscar dono
        8 - Exibir donos
        9 - Sair
        #====================================#
        """)
        
        option = str(input("Escolha uma opção no menu acima: "))

        if option == "1":
            Animal.adicionar_animal()
        elif option == "2":
            remover_animal()
        elif option == "3":
            buscar_animal()
        elif option == "4":
            exibir_animais()
        elif option == "5":
            

from animal import Animal, Cachorro, Gato

    
while True:
        print("""
        #========🐾 Menu Principal 🐕‍🦺========#
        1️⃣ - Adicionar animal 
        2️⃣ - Remover animal
        3️⃣ - Buscar animal
        4️⃣ - Exibir animais
        5️⃣ - Adicionar dono
        6️⃣ - Remover dono
        7️⃣ - Buscar dono
        8️⃣ - Exibir donos
        9️⃣ - Sair
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
            

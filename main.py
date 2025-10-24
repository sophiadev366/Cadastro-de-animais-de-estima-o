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
            print("\n===📋 Adicionar pet 📋===")
            nome = input("Nome: ")
            idade = input("Idade: ")
            dono = input("Dono: ")

            resultado = Animal.adicionar_animal(nome, idade, dono)
            print(f"\n Animal cadastrado com sucesso!" if resultado == True else resultado)

        elif option == "2":
            print("\n===❌Remover pet❌===")
            nome = input("insira o nome para a remoção do pet: ")

            resultado = Animal.remover_animal(nome)
            print(f"Animal removido com sucesso!" if resultado == True else "Não foi possível remover o Animal!")

        elif option == "3":
            print("\n===🔎Buscar pet🔍===")
            nome = input("insira o nome para buscar o pet: ")
            resultado = Animal.buscar_animal(nome)
            if not resultado:
                print("\nPet não encontrado!")
            else:
                print(f"\nNome: {resultado[0]} | CPF: {resultado[1]}")

        elif option == "4":
            print("\n===📑Exibir Usuários📑===")
            biblioteca.exibir_usuarios()

        elif option == "5":
            print("\n===📋 Adição de Livro 📋===")
            titulo = input("Título: ")
            ano = input("Ano: ")
            autor = input("Autor: ")
            genero = input("Gênero: ")
            resultado = biblioteca.adicionar_livro(titulo, ano, autor, genero)
            print("\nLivro adicionado com sucesso!" if resultado == True else resultado)

        elif option == "6":
            print("\n===❌Remoção de Livro❌===")
            titulo = input("insira o título para a remoção do livro: ")
            resultado = biblioteca.remover_livro(titulo)
            print(f"Livro removido com sucesso!" if resultado == True else "Não foi possível remover o Livro!")

        elif option == "7":
            print("\n===🔎Buscar Usuário🔍===")
            titulo = input("insira o título para buscar o livro: ")
            resultado = biblioteca.buscar_livro(titulo)
            if not resultado:
                print("\nLivro não encontrado!")
            else:
                print(f"titulo: {resultado[0]} | autor: {resultado[1]} | ano: {resultado[2]} | genero: {resultado[3]} | disponivel: {resultado[4]}")

        elif option == "8":
            print("\n===📖Exibir Livros📖===")
            biblioteca.exibir_livros()

 
        
        elif option == "13":
            biblioteca.salvar_usuarios()
            biblioteca.salvar_livros()
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":

    menu()
            

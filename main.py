from animal import Animal, Cachorro, Gato

def menu():
    while True:
        print("""
        #========🐾 Menu Principal 🐕‍🦺========#
        1️⃣ - Adicionar animal 
        2️⃣ - Remover animal
        3️⃣ - Buscar animal
        4️⃣ - Exibir animais
        9️⃣ - Sair
        #====================================#
        """)
        
        option = input("Escolha uma opção no menu acima: ")

        if option == "1":
            print("\n===📋 Adicionar Pet 📋===")
            nome = input("Nome: ")
            idade = input("Idade: ")
            dono = input("Dono: ")

            resultado = Animal.adicionar_animal(nome, idade, dono)
            print("\nAnimal cadastrado com sucesso!" if resultado else "Erro ao cadastrar!")

        elif option == "2":
            print("\n===❌ Remover Pet ❌===")
            nome = input("Nome do pet para remover: ")

            resultado = Animal.remover_animal(nome)
            print("Animal removido com sucesso!" if resultado else "Pet não encontrado!")

        elif option == "3":
            print("\n===🔎 Buscar Pet 🔍===")
            nome = input("Nome do pet para buscar: ")
            resultado = Animal.buscar_animal(nome)
            if not resultado:
                print("Pet não encontrado!")
            else:
                print(f"\nNome: {resultado[0]} | Idade: {resultado[1]} | Dono: {resultado[2]}")

        elif option == "4":
            print("\n===📑 Lista de Pets 📑===")
            Animal.exibir_animais()

        elif option == "9":
            print("Saindo do sistema... Até logo! 🐾")
            break

        else:
            print("⚠ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()

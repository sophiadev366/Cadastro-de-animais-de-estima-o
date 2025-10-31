from animal import Gerenciador

def mostrar_titulo():
    """
    Mostra o título do sistema.
    """
    print("=" * 40)
    print("   🐶 SISTEMA DE PET SHOP 🐱")
    print("=" * 40)
    print()

def menu():
    """
    Menu principal do sistema, com opções pré-condicionadas por perfil de usuário.
    """
    sistema = Gerenciador()
    perfil = ""

    # Seleção de perfil
    while perfil not in ["admin", "normal"]:
        perfil = input("Digite seu perfil (admin/normal): ").lower().strip()
        if perfil not in ["admin", "normal"]:
            print("❌ Perfil inválido! Digite 'admin' ou 'normal'.")

    continuar = True
    while continuar:
        mostrar_titulo()
        print("1️⃣  Cadastrar/Adicionar Animal" if perfil=="admin" else "")
        print("2️⃣  Remover Animal" if perfil=="admin" else "")
        print("3️⃣  Buscar Animal")
        print("4️⃣  Listar Animais")
        print("0️⃣  Sair")

        opcao = input("\n👉 Escolha uma opção: ").strip()

        # Opções para admin
        if perfil == "admin":
            if opcao == "1":
                sistema.cadastrar_animal()
            elif opcao == "2":
                sistema.remover_animal()
            elif opcao == "3":
                sistema.buscar_animal()
            elif opcao == "4":
                sistema.listar_animais()
            elif opcao == "0":
                print("Saindo do sistema... 👋")
                break
            else:
                print("\033[31m❌ Opção inválida!\033[0m")
        # Opções para usuário normal
        else:
            if opcao == "3":
                sistema.buscar_animal()
            elif opcao == "4":
                sistema.listar_animais()
            elif opcao == "0":
                print("Saindo do sistema... 👋")
                break
            else:
                print("\033[31m❌ Opção inválida!\033[0m")

        # Pergunta para continuar
        if opcao in ["1","2","3","4"]:
            while True:
                resposta = input("Deseja continuar no sistema? (s/n): ").lower().strip()
                if resposta == "s":
                    break
                elif resposta == "n":
                    print("Saindo do sistema...👋")
                    continuar = False
                    break
                else:
                    print("❌\033[31m Opção inválida! Digite 's' ou 'n'.\033[0m")

if __name__ == "__main__":
    menu()
    
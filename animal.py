import json

# ----- CLASSES -----
class Animal:
    """
    Classe base para todos os animais.
    """
    def __init__(self, nome, especie, raca, idade, dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono

    def to_dict(self):
        """
        Converte o objeto em dicionário para salvar em JSON.
        """
        return {
            "tipo": "Animal",
            "nome": self.nome,
            "especie": self.especie,
            "raca": self.raca,
            "idade": self.idade,
            "dono": self.dono
        }

    def __str__(self):
        """
        Retorna uma representação legível do animal.
        """
        return f"{self.especie} - Nome: {self.nome}, Raça: {self.raca}, Idade: {self.idade}, Dono: {self.dono}"
    
class Cachorro(Animal):
    """
    Classe Cachorro, herda de Animal.
    """
    def __init__(self, nome, raca, idade, dono):
        super().__init__(nome, "Cachorro", raca, idade, dono)

    def to_dict(self):
        """
        Sobrescreve o método para incluir tipo Cachorro.
        """
        return {
            "tipo": "Cachorro",
            "nome": self.nome,
            "raca": self.raca,
            "idade": self.idade,
            "dono": self.dono
        }

class Gato(Animal):
    """
    Classe Gato, herda de Animal.
    """
    def __init__(self, nome, raca, idade, dono):
        super().__init__(nome, "Gato", raca, idade, dono)

    def to_dict(self):
        """
        Sobrescreve o método para incluir tipo Gato.
        """
        return {
            "tipo": "Gato",
            "nome": self.nome,
            "raca": self.raca,
            "idade": self.idade,
            "dono": self.dono
        }
    
# ----- GERENCIADOR -----

class Gerenciador:
    """
    Classe responsável por gerenciar os animais e persistir dados.
    """
    def _init_(self, arquivo="animais.json"):
        self.arquivo = arquivo
        self.animais = self.carregar()

    def carregar(self):
        """
        Carrega os animais do arquivo JSON.
        """
        try:
            with open(self.arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                lista = []
                for d in dados:
                    tipo = d.get("tipo", "Animal")
                    if tipo == "Cachorro":
                        lista.append(Cachorro(d["nome"], d["raca"], d["idade"], d["dono"]))
                    elif tipo == "Gato":
                        lista.append(Gato(d["nome"], d["raca"], d["idade"], d["dono"]))
                    else:
                        lista.append(Animal(d["nome"], d["especie"], d["raca"], d["idade"], d["dono"]))
                return lista
        except FileNotFoundError:
            return []

    def salvar(self):
        """
        Salva os animais no arquivo JSON.
        """
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump([a.to_dict() for a in self.animais], f, indent=4, ensure_ascii=False)

    def cadastrar_animal(self):
        """
        Cadastra ou adiciona um animal (admin).
        """
        print("\n📝 Cadastrar/Adicionar Animal")
        nome = input("Nome do animal: ").strip()
        especie = input("Espécie (Cachorro/Gato/Outro): ").capitalize().strip()
        raca = input("Raça: ").strip()
        
        while True:
            idade = input("Idade: ").strip()
            if idade.isdigit() and int(idade) >= 0:
                idade = int(idade)
                break
            else:
                print("❌ Idade inválida. Digite um número inteiro positivo.")

        dono = input("Nome do dono: ").strip()

        if especie == "Cachorro":
            animal = Cachorro(nome, raca, idade, dono)
        elif especie == "Gato":
            animal = Gato(nome, raca, idade, dono)
        else:
            animal = Animal(nome, especie, raca, idade, dono)

        self.animais.append(animal)
        self.salvar()
        print(f"✅ Animal {animal.nome} cadastrado com sucesso!")

    def remover_animal(self):
        """
        Remove um animal pelo nome (admin).
        """
        if not self.animais:
            print("❌ Nenhum animal cadastrado. Cadastre pelo menos um animal antes de tentar remover.")
            return

        nome = input("Digite o nome do animal para remover: ").strip()
        animal = self.buscar_animal_por_nome(nome)
        if animal:
            self.animais.remove(animal)
            self.salvar()
            print(f"✅ Animal {nome} removido com sucesso!")
        else:
            print("❌ Animal não encontrado.")

    def buscar_animal(self):
        """
        Busca um animal pelo nome.
        """
        if not self.animais:
            print("❌ Nenhum animal cadastrado. Cadastre pelo menos um animal antes de buscar.")
            return

        nome = input("Digite o nome do animal: ").strip()
        animal = self.buscar_animal_por_nome(nome)
        if animal:
            print(f"\n🔍 Animal encontrado:\n{animal}")
        else:
            print("❌ Animal não encontrado.")

    def listar_animais(self):
        """
        Lista todos os animais de forma legível.
        """
        if not self.animais:
            print("❌ Nenhum animal cadastrado. Cadastre pelo menos um animal antes de tentar listar. ")
        else:
            print("\n📋 Animais cadastrados:")
            for i, a in enumerate(self.animais, 1):
                print(f"{i}. {a}")

    def buscar_animal_por_nome(self, nome):
        """
        Busca um animal pelo nome exatamente como foi cadastrado.
        """
        for a in self.animais:
            if a.nome == nome:  # comparação exata, respeita maiúsculas/minúsculas
                return a
        return None
    

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
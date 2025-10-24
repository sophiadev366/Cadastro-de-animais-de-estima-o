import animal

class CadastroDono:
    def __init__(self, nome, idade, email, animal):
        self.nome = nome
        self.idade = idade
        self.email = email
CadastroDono.animal = animal



def exibirInformacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"
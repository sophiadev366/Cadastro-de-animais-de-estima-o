# Cadastro de Animais
class Animal:
    def __init__(self, nome, idade, dono):
        self.nome = nome
        self.idade = idade
        self.dono = dono

    def emitirSom(self):
        print(f"{self.nome} faz um som.")

    def exibirDados(self):
        print(f'''
                Nome: {self.nome}
                Idade: {self.idade}
                Dono: {self.dono}
''')
        
    def adicionarAnimal(self, animal):
            self.animal.append(Animal(nome, idade, dono))
            
    def removerAnimal(self, animal):

        pass
    def buscarAnimal(self, nome):
        pass
    def exibirAnimais(self):
        pass


class Cachorro(Animal):
    def Cachorro(self, nome, idade, dono, raça):
        super().__init__(nome, idade, dono)
        self.raça = raça
    def emitirSom(self):
        print(f"{self.nome} late: Au Au!")
    def exibirDados(self):
        super().exibirDados()
        print(f"Raça: {self.raça}")

class Gato(Animal):
    def Gato(self, nome, idade, dono, cor):
        super().__init__(nome, idade, dono)
        self.cor = cor
    def emitirSom(self):
        print(f"{self.nome} mia: Miau Miau!")
    def exibirDados(self):
        super().exibirDados()
        print(f"Cor: {self.cor}")   







c=Animal("Rex", 5, "João")
c.exibirDados()
c.emitirSom()
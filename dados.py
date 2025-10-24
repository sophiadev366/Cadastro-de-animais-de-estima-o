class Dados:
    def __init__(self):
        self.animais = []
        self.donos = []

    def adicionar_animal(self, animal):
        self.animais.append(animal)

    def remover_animal(self, animal):
        self.animais.remove(animal)

    def buscar_animal(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                return animal
        return None
    
    def exibir_animais(self):
        for animal in self.animais:
            animal.exibirDados()

    def adicionar_dono(self, dono):
        self.donos.append(dono)

    def remover_dono(self, dono):
        self.donos.remove(dono)

    def buscar_dono(self, nome):
        for dono in self.donos:
            if dono.nome == nome:
                return dono
        return None
    
    def exibir_donos(self):
        for dono in self.donos:
            print(dono.exibirInformacoes())
            
dados = Dados()
def get_dados():
    return dados

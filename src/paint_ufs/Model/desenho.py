class Desenho:
    def __init__(self):
        self.figuras = []
        self.figura_nova = None

    def adicionar_figura(self, figura):
        self.figuras.append(figura)

    def definir_figura_nova(self, figura):
        self.figura_nova = figura

    def limpar_figura_nova(self):
        self.figura_nova = None

    def obter_figuras(self):
        return self.figuras
    
    def obter_figura_nova(self):
        return self.figura_nova
from abc import abstractmethod
from src.paint_ufs.Controller.ferramentas.ferramentas_de_desenho import FerramentaDesenho
from src.paint_ufs.Model.figura import Linha, Retangulo, Rabisco, Oval, Circulo


class FerramentaArrastar(FerramentaDesenho):

    @abstractmethod
    def criar_figura(self, event, view):
        raise NotImplementedError
    
    def pressionar(self, event, desenho, view):
        figura = self.criar_figura(event, view)
        desenho.definir_figura_nova(figura)

    def arrastar(self, event, desenho, view):
        figura_nova = desenho.obter_figura_nova()
        if figura_nova is None:
            return
        figura_nova.atualizar(event.x, event.y)

    def soltar(self, event, desenho, view):
        figura_nova = desenho.obter_figura_nova()
        if figura_nova is not None and not figura_nova.incompleta():
            desenho.adicionar_figura(figura_nova)
        desenho.limpar_figura_nova()


class FerramentaLinha(FerramentaArrastar):
    
    def criar_figura(self, event, view):
        cor_borda = view.obter_cor_borda()
        return Linha(event.x, event.y, event.x, event.y, cor_borda)
    
class FerramentaRabisco(FerramentaArrastar):

    def criar_figura(self, event, view):
        cor_borda = view.obter_cor_borda()
        return Rabisco([(event.x, event.y)], cor_borda)
    
class FerramentaRetangulo(FerramentaArrastar):
    
    def criar_figura(self, event, view):
        cor_borda = view.obter_cor_borda()
        cor_preenchimento = view.obter_cor_preenchimento()
        return Retangulo(event.x, event.y, event.x, event.y, cor_borda, cor_preenchimento )
    
class ferramentaOval(FerramentaArrastar):

    def criar_figura(self, event, view):
        cor_borda = view.obter_cor_borda()
        cor_preenchimento = view.obter_cor_preenchimento()
        return Oval(event.x, event.y, event.x, event.y, cor_borda, cor_preenchimento)
    
class FerramentaCirculo(FerramentaArrastar):

    def criar_figura(self, event, view):
        cor_borda = view.obter_cor_borda()
        cor_preenchimento = view.obter_cor_preenchimento()
        return Circulo(event.x, event.y, event.x, event.y, cor_borda, cor_preenchimento)
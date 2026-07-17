from abc import ABC, abstractmethod

class FerramentaDesenho(ABC):

    @abstractmethod
    def pressionar(self, event, desenho, view):
        raise NotImplementedError
    
    def arrastar(self, event, desenho, view):
        pass

    def soltar(self, event, desenho, view):
        pass

    def mover(self, event, desenho, view):
        pass

    def finalizar(self, event, desenho, view):
        pass
#Falta atualizar o formas.py inplementando o ferramentas_de_arrastar e futuramente o ferramenta_poligono (quando fizer isso apague essa mensagem) Ass. Gustavo


from src.paint_ufs.Model.desenho import Desenho
from src.paint_ufs.Controller.ferramentas.ferramenta_de_arrastar import (
    FerramentaLinha, FerramentaRabisco, FerramentaRetangulo,
    ferramentaOval, FerramentaCirculo,
)
from src.paint_ufs.Controller.ferramentas.ferramenta_poligono import FerramentaPoligono



class Controller:
    def __init__(self, view):
        self.view = view
        self.desenho = Desenho()
        self.ferramentas = {
            "Linha": FerramentaLinha(),
            "Retangulo": FerramentaRetangulo(),
            "Oval": ferramentaOval(),
            "Circulo": FerramentaCirculo(),
            "Rabisco": FerramentaRabisco(),
            "Poligono": FerramentaPoligono(),
        } 
        
        self._registrar_binds()



    def _registrar_binds(self):
        
        self.view.bind_canvas('<ButtonPress-1>', self._on_pressionar)
        self.view.bind_canvas('<B1-Motion>', self._on_arrastar)
        self.view.bind_canvas('<ButtonRelease-1>', self._on_soltar)
        self.view.bind_canvas('<Motion>', self._on_mover)
        self.view.bind_canvas('<Double-Button-1>', self._on_finalizar)
        self.view.bind_canvas('<Button-3>', self._on_finalizar)



    def _ferramenta_atual(self):
        tipo = self.view.obter_tipo_figura()
        return self.ferramentas.get(tipo)

    def _on_pressionar(self, event):
        ferramenta = self._ferramenta_atual()
        if ferramenta is None:
            return
        ferramenta.pressionar(event, self.desenho, self.view)
        self._redesenhar()

    def _on_arrastar(self, event):
        ferramenta = self._ferramenta_atual()
        if ferramenta is None:
            return
        ferramenta.arrastar(event, self.desenho, self.view)
        self._redesenhar()

    def _on_soltar(self, event):
        ferramenta = self._ferramenta_atual()
        if ferramenta is None:
            return
        ferramenta.soltar(event, self.desenho, self.view)
        self._redesenhar()

    def _on_mover(self, event):
        ferramenta = self._ferramenta_atual()
        if ferramenta is None:
            return
        ferramenta.mover(event, self.desenho, self.view)
        self._redesenhar()

    def _on_finalizar(self, event):
        ferramenta = self._ferramenta_atual()
        if ferramenta is None:
            return
        ferramenta.finalizar(event, self.desenho, self.view)
        self._redesenhar()

    def _redesenhar(self):
        self.desenhar_figuras()
        self.desenhar_figura_nova()



    def desenhar_figuras(self):
        self.view.limpar_canvas()
        for figura in self.desenho.obter_figuras():
            self.view.desenhar_figura(figura)

    def desenhar_figura_nova(self):
        figura_nova = self.desenho.obter_figura_nova()
        if figura_nova is not None:
            self.view.desenhar_figura(figura_nova, preview=True)

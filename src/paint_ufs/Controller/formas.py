
from src.paint_ufs.Model.figura import Linha, Retangulo, Oval, Circulo, Rabisco, Poligono
from src.paint_ufs.Model.desenho import Desenho


CLASSES_FIGURA= {  "Linha": Linha,
                "Retangulo": Retangulo,
                 "Oval": Oval,
              "Circulo": Circulo,
                 "Rabisco": Rabisco,
                 "Poligono": Poligono,}


class Controller:
    def __init__(self, view):
        self.view = view
        self.desenho = Desenho()
        self._registrar_binds()



    def _registrar_binds(self):
        self.view.bind_canvas('<ButtonPress-1>', self.iniciar_figura_nova)
        self.view.bind_canvas('<B1-Motion>', self.atualizar_figura_nova)
        self.view.bind_canvas('<ButtonRelease-1>', self.incluir_figura_nova)
        self.view.bind_canvas('<Motion>', self.mover_mouse)
        self.view.bind_canvas('<Double-Button-1>', self.finalizar_poligono)
        self.view.bind_canvas('<Button-3>', self.finalizar_poligono)



# Quando mouse é pressionado
    def iniciar_figura_nova(self, event):
        tipo = self.view.obter_tipo_figura()
        cor_borda = self.view.obter_cor_borda()
        cor_preenchimento = self.view.obter_cor_preenchimento()

        if tipo == 'Poligono':
            self._iniciar_ou_continuar_poligono(event)
            return

        if tipo == 'Linha':
            figura = Linha(event.x, event.y, event.x, event.y, cor_borda)
        elif tipo == 'Rabisco':
            figura = Rabisco([(event.x, event.y)], cor_borda)
        elif tipo in CLASSES_FIGURA:
            classe = CLASSES_FIGURA[tipo]
            figura = classe(event.x, event.y, event.x, event.y,
                             cor_borda, cor_preenchimento)
        else:
            return
        

        self.desenho.definir_figura_nova(figura)

# Quando mouse é movido com o botão pressionado
    def atualizar_figura_nova(self, event):
        figura_nova = self.desenho.obter_figura_nova()
        if figura_nova is None or isinstance(figura_nova, Poligono):
            return
        figura_nova.atualizar(event.x, event.y)

        self.desenhar_figuras()
        self.desenhar_figura_nova()

# Quando mouse é solto
    def incluir_figura_nova(self, event):
        figura_nova = self.desenho.obter_figura_nova()
        if isinstance(figura_nova, Poligono):
            return  # polígono só é incluído quando finalizado (duplo-clique)
        if figura_nova is not None and not figura_nova.incompleta():
            self.desenho.adicionar_figura(figura_nova)
        self.desenho.limpar_figura_nova()
        self.desenhar_figuras()

    def _iniciar_ou_continuar_poligono(self, event):
        figura_nova = self.desenho.obter_figura_nova()

        if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
            figura_nova.adicionar_ponto(event.x, event.y)
        else:
            cor_borda = self.view.obter_cor_borda()
            cor_preenchimento = self.view.obter_cor_preenchimento()
            figura_nova = Poligono(event.x, event.y, cor_borda, cor_preenchimento)
            self.desenho.definir_figura_nova(figura_nova)
        self.desenhar_figuras()
        self.desenhar_figura_nova()
 
    def mover_mouse(self, event):
        """Chamado em <Motion> (mouse se movendo, sem botão pressionado).
        Usado apenas para mostrar a prévia do próximo segmento do polígono."""
        figura_nova = self.desenho.obter_figura_nova()
        if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
            figura_nova.atualizar_preview(event.x, event.y)
            self.desenhar_figuras()
            self.desenhar_figura_nova()
 
 
    def finalizar_poligono(self, event):
        """Chamado em duplo-clique (ou clique direito) para fechar o polígono."""
        figura_nova = self.desenho.obter_figura_nova()
        if isinstance(figura_nova, Poligono):
            figura_nova.finalizar()
            if not figura_nova.incompleta():
                self.desenho.adicionar_figura(figura_nova)
            self.desenho.limpar_figura_nova()
            self.desenhar_figuras()



    def desenhar_figuras(self):
        self.view.limpar_canvas()
        for figura in self.desenho.obter_figuras():
            self.view.desenhar_figura(figura)

    def desenhar_figura_nova(self):
        figura_nova = self.desenho.obter_figura_nova()
        if figura_nova is not None:
            self.view.desenhar_figura(figura_nova, preview=True)


from src.paint_ufs.Model.figura import Linha, Retangulo, Oval, Circulo, Rabisco, Poligono



CLASSES_FIGURA= {  "Linha": Linha,
                "Retangulo": Retangulo,
                 "Oval": Oval,
              "Circulo": Circulo,
                 "Rabisco": Rabisco,
                 "Poligono": Poligono,}
class Controller:
    def __init__(self, canvas, tipo_figura_var, cor_borda_atual, cor_preenchimento_atual, preencher_var,figura_nova):
        self.canvas= canvas
        self.tipo_figura_var= tipo_figura_var
        self.cor_borda_atual = cor_borda_atual
        self.cor_preenchimento_atual = cor_preenchimento_atual   
        self.preencher_var = preencher_var

        self.figuras = []
        self.figura_nova = figura_nova



    def obter_cor_preenchimento(self):
        """Retorna a cor de preenchimento a usar, ou '' (transparente) se a opção de preencher estiver desligada."""
        if self.preencher_var.get():
            return self.cor_preenchimento_atual.get()
        return ''



# Quando mouse é pressionado
    def iniciar_figura_nova(self, event):
     
        tipo = self.tipo_figura_var.get()
        cor_borda = self.cor_borda_atual.get()
        cor_preenchimento = self.obter_cor_preenchimento()
    
        if tipo =='Poligono':
            self._iniciar_ou_continuar_poligono(event)
            return
    
    
        if tipo == 'Linha':
            self.figura_nova = Linha(event.x, event.y, event.x, event.y, cor_borda)
        elif tipo == 'Rabisco':
            self.figura_nova = Rabisco([(event.x, event.y)], cor_borda)
        elif tipo in CLASSES_FIGURA:
            classe = CLASSES_FIGURA[tipo]
            self.figura_nova = classe(event.x, event.y, event.x, event.y,
                          cor_borda, cor_preenchimento)
        
# Quando mouse é movido com o botão pressionado
    def atualizar_figura_nova(self, event):
        if self.figura_nova is None or isinstance(self.figura_nova, Poligono):
            return
        self.figura_nova.atualizar(event.x, event.y)
    
        self.desenhar_figuras()
        self.desenhar_figura_nova()

# Quando mouse é solto
    def incluir_figura_nova(self, event): 
        if isinstance(self.figura_nova, Poligono):
            return  # polígono só é incluído quando finalizado (duplo-clique)
        if self.figura_nova is not None and not self.figura_nova.incompleta():
             self.figuras.append(self.figura_nova)
        self.figura_nova= None     
        self.desenhar_figuras()

    def _iniciar_ou_continuar_poligono(self, event):
        
        if isinstance(self.figura_nova, Poligono) and not self.figura_nova.finalizado:
            self.figura_nova.adicionar_ponto(event.x, event.y)
        else:
            cor_borda = self.cor_borda_atual.get()
            cor_preenchimento = self.obter_cor_preenchimento()
            self.figura_nova = Poligono(event.x, event.y, cor_borda, cor_preenchimento)
        self.desenhar_figuras()
        self.desenhar_figura_nova()
 
 
    def mover_mouse(self, event):
        """Chamado em <Motion> (mouse se movendo, sem botão pressionado).
        Usado apenas para mostrar a prévia do próximo segmento do polígono."""
        if isinstance(self.figura_nova, Poligono) and not self.figura_nova.finalizado:
            self.figura_nova.atualizar_preview(event.x, event.y)
            self.desenhar_figuras()
            self.desenhar_figura_nova()
 
 
    def finalizar_poligono(self, event):
        """Chamado em duplo-clique (ou clique direito) para fechar o polígono."""
        
        if isinstance(self.figura_nova, Poligono):
            self.figura_nova.finalizar()
            if not self.figura_nova.incompleta():
                self.figuras.append(self.figura_nova)
            self.figura_nova = None
            self.desenhar_figuras()



    def desenhar_figuras(self):
        self.canvas.delete("all")
        for figura in self.figuras:
            figura.desenhar(self.canvas)

    def desenhar_figura_nova(self):
        if self.figura_nova is not None:
            self.figura_nova.desenhar(self.canvas, preview=True)

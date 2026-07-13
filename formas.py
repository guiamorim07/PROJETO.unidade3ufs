
from figura import Linha, Retangulo, Oval, Circulo, Rabisco, Poligono


canvas = None
tipo_figura_var = None
cor_borda_atual = None
cor_preenchimento_atual = None
preencher_var = None


figuras = []
figura_nova = None


    
CLASSES_FIGURA= {  "Linha": Linha,
                "Retangulo": Retangulo,
                 "Oval": Oval,
              "Circulo": Circulo,
                 "Rabisco": Rabisco,
                 "Poligono": Poligono,}

def obter_cor_preenchimento():
    """Retorna a cor de preenchimento a usar, ou '' (transparente) se a opção de preencher estiver desligada."""
    if preencher_var.get():
        return cor_preenchimento_atual.get()
    return ''



# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    
    tipo = tipo_figura_var.get()
    cor_borda = cor_borda_atual.get()
    cor_preenchimento = obter_cor_preenchimento()
    
    if tipo =='Poligono':
        _iniciar_ou_continuar_poligono(event)
        return
    
    
    if tipo == 'Linha':
        figura_nova = Linha(event.x, event.y, event.x, event.y, cor_borda)
    elif tipo in CLASSES_FIGURA:
        classe = CLASSES_FIGURA[tipo]
        figura_nova = classe(event.x, event.y, event.x, event.y,
                              cor_borda, cor_preenchimento)
    else:  
        figura_nova = Rabisco([(event.x, event.y)], cor_borda)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    if figura_nova is None or isinstance(figura_nova, Poligono):
        return
    figura_nova.atualizar(event.x, event.y)
    
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if isinstance(figura_nova, Poligono):
        return  # polígono só é incluído quando finalizado (duplo-clique)
    if figura_nova is not None and not figura_nova.incompleta():
        figuras.append(figura_nova)
    desenhar_figuras()

def _iniciar_ou_continuar_poligono(event):
    global figura_nova
    if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
        figura_nova.adicionar_ponto(event.x, event.y)
    else:
        cor_borda = cor_borda_atual.get()
        cor_preenchimento = obter_cor_preenchimento()
        figura_nova = Poligono(event.x, event.y, cor_borda, cor_preenchimento)
    desenhar_figuras()
    desenhar_figura_nova()
 
 
def mover_mouse(event):
    """Chamado em <Motion> (mouse se movendo, sem botão pressionado).
    Usado apenas para mostrar a prévia do próximo segmento do polígono."""
    if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
        figura_nova.atualizar_preview(event.x, event.y)
        desenhar_figuras()
        desenhar_figura_nova()
 
 
def finalizar_poligono(event):
    """Chamado em duplo-clique (ou clique direito) para fechar o polígono."""
    global figura_nova
    if isinstance(figura_nova, Poligono):
        figura_nova.finalizar()
        if not figura_nova.incompleta():
            figuras.append(figura_nova)
        figura_nova = None
        desenhar_figuras()



def desenhar_figuras():
    canvas.delete("all")
    for figura in figuras:
        figura.desenhar(canvas)

def desenhar_figura_nova():
    if figura_nova is not None:
        figura_nova.desenhar(canvas, preview=True)

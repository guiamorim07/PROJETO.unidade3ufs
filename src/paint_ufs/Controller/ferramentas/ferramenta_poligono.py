from src.paint_ufs.Controller.ferramentas.ferramentas_de_desenho import FerramentaDesenho
from src.paint_ufs.Model.figura import Poligono


class FerramentaPoligono(FerramentaDesenho):
    """
    Diferente da FerramentaArrastar, o polígono não segue pressionar->arrastar->soltar.
    Ele é construído por uma sequência de cliques (pressionar) e finalizado
    separadamente (duplo-clique / botão direito).
    """

    def pressionar(self, event, desenho, view):
        figura_nova = desenho.obter_figura_nova()

        if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
            figura_nova.adicionar_ponto(event.x, event.y)
        else:
            cor_borda = view.obter_cor_borda()
            cor_preenchimento = view.obter_cor_preenchimento()
            figura_nova = Poligono(event.x, event.y, cor_borda, cor_preenchimento)
            desenho.definir_figura_nova(figura_nova)

    # arrastar e soltar ficam como no-op (herdados da base)
    # polígono não usa arrastar-e-soltar do mouse.

    def mover(self, event, desenho, view):
        figura_nova = desenho.obter_figura_nova()
        if isinstance(figura_nova, Poligono) and not figura_nova.finalizado:
            figura_nova.atualizar_preview(event.x, event.y)

    def finalizar(self, event, desenho, view):
        figura_nova = desenho.obter_figura_nova()
        if isinstance(figura_nova, Poligono):
            figura_nova.finalizar()
            if not figura_nova.incompleta():
                desenho.adicionar_figura(figura_nova)
            desenho.limpar_figura_nova()
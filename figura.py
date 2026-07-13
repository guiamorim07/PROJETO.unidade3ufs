"""Arquivo criado para a atualização do código (P.I -> P.O.O)"""

class Figura:
    """Classe base abstrata para todas as figuras."""
 
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento
 
    def desenhar(self, canvas, preview=False):
        """Desenha a figura no canvas. Se preview=True, é a figura ainda
        em construção (mostrada com borda pontilhada)."""
        raise NotImplementedError
 
    def atualizar(self, x, y):
        """Atualiza a figura enquanto o usuário arrasta o mouse."""
        raise NotImplementedError
 
    def incompleta(self):
        """Indica se a figura ainda não tem tamanho/forma válida para
        ser incluída na lista definitiva de figuras."""
        raise NotImplementedError
 
 
class Linha(Figura):
    def __init__(self, x0, y0, x1, y1, cor_borda):
        super().__init__(cor_borda, '')
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
 
    def desenhar(self, canvas, preview=False):
        canvas.create_line(self.x0, self.y0, self.x1, self.y1,
                            dash=(4, 2) if preview else None,
                            fill=self.cor_borda)
 
    def atualizar(self, x, y):
        self.x1 = x
        self.y1 = y
 
    def incompleta(self):
        return (self.x0, self.y0) == (self.x1, self.y1)
 
 
class FiguraDoisPontos(Figura):
    """Base para figuras definidas por dois pontos opostos (um retângulo
    envolvente): Retangulo, Oval e Circulo."""
 
    def __init__(self, x0, y0, x1, y1, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
 
    def atualizar(self, x, y):
        self.x1 = x
        self.y1 = y
 
    def incompleta(self):
        return (self.x0 == self.x1) or (self.y0 == self.y1)
 
    def _cor_preenchimento_desenho(self, preview):
        return self.cor_preenchimento if not (preview and self.incompleta()) else ''
 
 
class Retangulo(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        canvas.create_rectangle(
            self.x0, self.y0, self.x1, self.y1,
            outline=self.cor_borda,
            fill=self._cor_preenchimento_desenho(preview),
            dash=(4, 2) if preview else None
        )
 
 
class Oval(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        canvas.create_oval(
            self.x0, self.y0, self.x1, self.y1,
            outline=self.cor_borda,
            fill=self._cor_preenchimento_desenho(preview),
            dash=(4, 2) if preview else None
        )
 
 
class Circulo(Oval):
    def atualizar(self, x, y):
        lado = max(abs(x - self.x0), abs(y - self.y0))
        self.x1 = self.x0 + lado if x >= self.x0 else self.x0 - lado
        self.y1 = self.y0 + lado if y >= self.y0 else self.y0 - lado
 
    def incompleta(self):
        return self.x0 == self.x1
 
 
class Rabisco(Figura):
    def __init__(self, pontos, cor_borda):
        super().__init__(cor_borda, '')
        self.pontos = pontos
 
    def desenhar(self, canvas, preview=False):
        if len(self.pontos) > 1:
            canvas.create_line(self.pontos, fill=self.cor_borda,
                                dash=(4, 2) if preview else None)
 
    def atualizar(self, x, y):
        self.pontos.append((x, y))
 
    def incompleta(self):
        return len(self.pontos) <= 1
 
 
class Poligono(Figura):
    """
    Diferente das demais figuras (que usam arrastar-e-soltar), o polígono
    é construído por uma sequência de cliques:
      - cada clique esquerdo adiciona um vértice
      - o movimento do mouse mostra uma prévia do próximo segmento
      - um duplo-clique (ou clique direito) finaliza o polígono
    """
 
    def __init__(self, x, y, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.pontos = [(x, y)]
        self.ponto_preview = None
        self.finalizado = False
 
    def adicionar_ponto(self, x, y):
        self.pontos.append((x, y))
 
    def atualizar_preview(self, x, y):
        self.ponto_preview = (x, y)
 
    def finalizar(self):
        self.finalizado = True
        self.ponto_preview = None
 
    def atualizar(self, x, y):
        # mantém a mesma interface de Figura; quem controla a construção
        # de fato (adicionar vértice x mostrar prévia) é o formas.py
        self.atualizar_preview(x, y)
 
    def desenhar(self, canvas, preview=False):
        pontos = list(self.pontos)
        if preview and self.ponto_preview and not self.finalizado:
            pontos = pontos + [self.ponto_preview]
 
        if len(pontos) < 2:
            return
 
        if self.finalizado and len(self.pontos) >= 3:
            canvas.create_polygon(pontos, outline=self.cor_borda,
                                   fill=self.cor_preenchimento,
                                   dash=(4, 2) if preview else None)
        else:
            canvas.create_line(pontos, fill=self.cor_borda,
                                dash=(4, 2) if preview else None)
 
    def incompleta(self):
        return (not self.finalizado) or len(self.pontos) < 3
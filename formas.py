# funções tipo desenhar_circulo(), desenhar_quadrado()...

from tkinter import *
from tkinter import ttk

canvas = None
tipo_figura_var = None
cor_borda_atual = None
cor_preenchimento_atual = None
preencher_var = None


figuras = []
figura_nova = None

FIGURAS_COM_PREENCHIMENTO = ('retangulo', 'oval', 'circulo')

def obter_cor_preenchimento():
    """Retorna a cor de preenchimento a usar, ou '' (transparente) se a opção de preencher estiver desligada."""
    if preencher_var.get():
        return cor_preenchimento_atual.get()
    return ''



# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    
    cor_borda = cor_borda_atual.get()
    cor_preenchimento = obter_cor_preenchimento()
    
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Oval':
        figura_nova = ('oval', (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo_figura_var.get() == 'Circulo':
        figura_nova = ('circulo', (event.x, event.y, event.x, event.y), cor_borda, cor_preenchimento)
    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_borda, cor_preenchimento)

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    tipo, values, cor_borda, cor_preenchimento = figura_nova
    if tipo == "rabisco":
        values.append((event.x, event.y))
        figura_nova = (tipo, values, cor_borda, cor_preenchimento)
    elif tipo == 'retangulo':
        figura_nova = ('retangulo', (values[0], values[1], event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo == 'oval':
        figura_nova = ('oval', (values[0], values[1], event.x, event.y), cor_borda, cor_preenchimento)
    elif tipo == 'circulo':
        x0, y0 = values[0], values[1]
        dx = event.x - x0
        dy = event.y - y0
        lado = max(abs(dx), abs(dy))
        x1 = x0 + lado if dx >= 0 else x0 - lado
        y1 = y0 + lado if dy >= 0 else y0 - lado
        figura_nova = ('circulo', (x0, y0, x1, y1), cor_borda, cor_preenchimento)
    else:  # tipo == "linha"
        figura_nova = ("linha", (values[0], values[1], event.x, event.y), cor_borda, cor_preenchimento)
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): 
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor_borda, cor_preenchimento in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda)
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3],
                                     outline=cor_borda, fill=cor_preenchimento)
        elif fig == 'oval':
            canvas.create_oval(values[0], values[1], values[2], values[3],
                                outline=cor_borda, fill=cor_preenchimento)
        elif fig == 'circulo':
            canvas.create_oval(values[0], values[1], values[2], values[3],
                                outline=cor_borda, fill=cor_preenchimento)
        else:  # fig == "rabisco"
            canvas.create_line(values, fill=cor_borda)

def desenhar_figura_nova():
    
    fig, values, cor_borda, cor_preenchimento = figura_nova
    preenchimento = cor_preenchimento if not incompleta(figura_nova) else ''
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cor_borda, dash=(4, 2))
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3],
                                 outline=cor_borda, fill=preenchimento, dash=(4, 2))
    elif fig == 'oval':
        canvas.create_oval(values[0], values[1], values[2], values[3],
                            outline=cor_borda, fill=preenchimento, dash=(4, 2))
    elif fig == 'circulo':
        canvas.create_oval(values[0], values[1], values[2], values[3],
                            outline=cor_borda, fill=preenchimento, dash=(4, 2))
    else:  # fig == "rabisco"
        canvas.create_line(values, fill=cor_borda, dash=(4, 2))

def incompleta(figura):
    fig, values, cor_borda, cor_preenchimento = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'retangulo':
        return values[0] == values[2] or values[1] == values[3]
    elif fig == 'oval':
        return values[0] == values[2] or values[1] == values[3]
    elif fig == 'circulo':
        return values[0] == values[2]
    else:  # fig == "rabisco"
        return len(values) <= 1






#Criei hierarquia de classes Figura (Linha, FiguraDoisPontos, Retangulo, Oval, Circulo, Rabisco) com métodos desenhar, atualizar e incompleta
# falta colocar o código de desenho para usar essas classes e definir se ficara em formas.py ou vao criar uma nova classe para gerenciar as figuras e o canvas
# deixei ela aqui para não perder o código que já estava feito, mas podemos mover para outro arquivo se for melhor organizar assim
#lemnbrando que ainda falta fazer a forma poligonos e demais atividades
# Ass: Gustavo"



class Figura:
    def __init__(self, cor_borda, cor_preenchimento):
        self.cor_borda = cor_borda
        self.cor_preenchimento = cor_preenchimento

    def desenhar(self, canvas, preview=False): 
        pass

    def atualizar(self, x, y): 
        pass

    def incompleta(self):
        pass

class Linha(Figura):
    def __init__(self, x0, x1, y0, y1, cor_borda):
        super().__init__(cor_borda, '')
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def desenhar(self, canvas, preview=False):
        canvas.create_line(self.x0, self.y0, self.x1, self.y1, dash=(4, 2) if preview else None, fill=self.cor_borda)

    def atualizar(self, x, y):
        self.x1 = x
        self.y1 = y

    def incompleta(self):
        return (self.x0, self.y0) == (self.x1, self.y1)
    


class FiguraDoisPontos(Figura):
    def __init__(self, x0, x1, y0, y1, cor_borda, cor_preenchimento):
        super().__init__(cor_borda, cor_preenchimento)
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

    def atualizar(self, x, y):
        self.x1 = x
        self.y1 = y

    def incompleta(self):
        return (self.x0 == self.x1) or (self.y0 == self.y1)

class Retangulo(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1, outline=self.cor_borda, fill=self.cor_preenchimento if not self.incompleta() else '', dash=(4, 2) if preview else None)

class Oval(FiguraDoisPontos):
    def desenhar(self, canvas, preview=False):
        canvas.create_oval(self.x0, self.y0, self.x1, self.y1, outline=self.cor_borda, fill=self.cor_preenchimento if not self.incompleta() else '', dash=(4, 2) if preview else None)

class Circulo(Oval):
    def atualizar(self, x, y):
        lado = max(abs(x - self.x0), abs(y - self.y0))
        self.x1 = self.x0 + lado if x >= self.x0 else self.x0 - lado
        self.y1 = self.y0 + lado if y >= self.y0 else self.y0 - lado

class Rabisco(Figura):
    def __init__(self, pontos, cor_borda):
        super().__init__(cor_borda, "")
        self.pontos = pontos

    def desenhar(self, canvas, preview=False):
        canvas.create_line(self.pontos, fill=self.cor_borda, dash=(4,2) if preview else None)

    def atualizar(self, x, y):
        self.pontos.append((x, y))

    def incompleta(self):
        return len(self.pontos) <= 1
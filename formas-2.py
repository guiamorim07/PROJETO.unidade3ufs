# funções tipo desenhar_circulo(), desenhar_quadrado()...

from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y), cor_atual.get()) 
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y), cor_atual.get())
    else :
        figura_nova = ("rabisco", [(event.x, event.y)], cor_atual.get())

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    tipo, values, cor = figura_nova
    if tipo == "rabisco":
        values.append((event.x, event.y))
        figura_nova = (tipo, values, cor)
    elif tipo == 'retangulo':
        figura_nova = ('retangulo', (values[0], values[1], event.x, event.y), cor)
    else : # tipo == "linha"
        figura_nova = ("linha", (values[0], values[1], event.x, event.y), cor)
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values, cor in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3], fill=cor)
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor)
        else : # fig == "rabisco"
            canvas.create_line(values, fill=cor)

def desenhar_figura_nova():
    fig, values, cor = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], fill=cor, dash=(4, 2))
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], outline=cor, dash=(4, 2))
    else : # fig == "rabisco"
        canvas.create_line(values, fill=cor, dash=(4, 2))

def incompleta(figura):
    fig, values, cor = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'retangulo':
        return values[0] == values[2] or values[1] == values[3] 
    else : # fig == "rabisco"
        return len(values) <= 1

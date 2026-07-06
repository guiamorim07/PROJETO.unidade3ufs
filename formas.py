# funções tipo desenhar_circulo(), desenhar_quadrado()...

from tkinter import *
from tkinter import ttk

# Quando mouse é pressionado
def iniciar_figura_nova(event): 
    global figura_nova
    if tipo_figura_var.get() == 'Linha':
        figura_nova = ("linha", (event.x, event.y, event.x, event.y))
    elif tipo_figura_var.get() == 'Retangulo':
        figura_nova = ('retangulo', (event.x, event.y, event.x, event.y))
    else :
        figura_nova = ("rabisco", [(event.x, event.y)])

# Quando mouse é movido com o botão pressionado
def atualizar_figura_nova(event):
    global figura_nova
    if figura_nova[0] == "rabisco":
        figura_nova[1].append((event.x, event.y))
    elif figura_nova[0] == 'retangulo':
        figura_nova = ('retangulo', (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    else : # figura_nova[0] == "linha"
        figura_nova = ("linha", (figura_nova[1][0], figura_nova[1][1], event.x, event.y))
    desenhar_figuras()
    desenhar_figura_nova()

# Quando mouse é solto
def incluir_figura_nova(event): 
    if not incompleta(figura_nova): # para evitar incluir figuras incompletas, como uma linha sem comprimento ou um rabisco com um único ponto
        figuras.append(figura_nova) 
    desenhar_figuras()

def desenhar_figuras():
    canvas.delete("all")
    for fig, values in figuras:
        if fig == "linha":
            canvas.create_line(values[0], values[1], values[2], values[3])
        elif fig == 'retangulo':
            canvas.create_rectangle(values[0], values[1], values[2], values[3])
        else : # fig == "rabisco"
            canvas.create_line(values)

def desenhar_figura_nova():
    fig, values = figura_nova
    if fig == "linha":
        canvas.create_line(values[0], values[1], values[2], values[3], dash=(4, 2))
    elif fig == 'retangulo':
        canvas.create_rectangle(values[0], values[1], values[2], values[3], dash=(4, 2))
    else : # fig == "rabisco"
        canvas.create_line(values, dash=(4, 2))

def incompleta(figura):
    fig, values = figura
    if fig == "linha":
        return (values[0], values[1]) == (values[2], values[3])
    elif fig == 'retangulo':
        return values[0] == values[2] or values[1] == values[3] 
    else : # fig == "rabisco"
        return len(values) <= 1





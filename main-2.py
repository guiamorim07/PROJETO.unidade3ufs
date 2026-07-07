#From formas import

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

# ponto de entrada, criaremos a janela e chamaremos as funcoes

figuras = []       # Todas as figuras desenhadas
figura_nova = None # Figura que esta sendo desenhada, mas ainda nao foi incluida em figuras

root = Tk()
frame = Frame(root)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

# label
label = ttk.Label(frame,  text='Paint:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu (linha ou rabisco)
option_menu = ttk.OptionMenu(frame, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retangulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# cor atual usada para desenhar novas figuras
cor_atual = StringVar(root, value='black')

# abre o seletor de cor do sistema e guarda a cor escolhida para as próximas figuras
def escolher_cor():
    cor = colorchooser.askcolor(title="Escolha a cor")[1]  # [1] retorna o valor em hexadecimal
    if cor:
        cor_atual.set(cor)
        cor_preview.config(background=cor)

# botão de escolher cor
botao_cor = ttk.Button(frame, text='Escolher cor', command=escolher_cor)
botao_cor.grid(column=2, row=0, sticky=W, **paddings)

# preview da cor selecionada
cor_preview = Canvas(frame, width=20, height=20, background='black', highlightthickness=1, highlightbackground='gray')
cor_preview.grid(column=3, row=0, sticky=W, **paddings)

# Area de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=4, sticky=W, **paddings)

frame.pack()

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()

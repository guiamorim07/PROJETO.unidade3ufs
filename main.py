#From formas import

from tkinter import *
from tkinter import ttk
import formas
from formas import iniciar_figura_nova, atualizar_figura_nova, incluir_figura_nova
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
                             'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

# Area de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()

formas.canvas = canvas
formas.tipo_figura_var = tipo_figura_var

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
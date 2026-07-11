#From formas import

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
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
                             'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

cor_borda_atual = StringVar(root, value='black')
 
# cor de preenchimento usada para desenhar novas figuras (retangulo, oval, circulo)
cor_preenchimento_atual = StringVar(root, value='red')
 
# controla se o preenchimento deve ser aplicado às novas figuras
preencher_var = BooleanVar(root, value=False)
 
 
####MAIN
# abre o seletor de cor do sistema e guarda a cor de borda escolhida
def escolher_cor_borda():
    cor = colorchooser.askcolor(title="Escolha a cor da borda")[1]  # [1] retorna o valor em hexadecimal
    if cor:
        cor_borda_atual.set(cor)
        cor_borda_preview.config(background=cor)
 
 
####MAIN
# abre o seletor de cor do sistema e guarda a cor de preenchimento escolhida
def escolher_cor_preenchimento():
    cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
    if cor:
        cor_preenchimento_atual.set(cor)
        cor_preenchimento_preview.config(background=cor)
 
 
####MAIN
# botão de escolher cor da borda
botao_cor_borda = ttk.Button(frame, text='Cor da borda', command=escolher_cor_borda)
botao_cor_borda.grid(column=2, row=0, sticky=W, **paddings)
 
# preview da cor de borda selecionada
cor_borda_preview = Canvas(frame, width=20, height=20, background='black',
                            highlightthickness=1, highlightbackground='gray')
cor_borda_preview.grid(column=3, row=0, sticky=W, **paddings)
 
# botão de escolher cor de preenchimento
botao_cor_preenchimento = ttk.Button(frame, text='Cor de preenchimento', command=escolher_cor_preenchimento)
botao_cor_preenchimento.grid(column=4, row=0, sticky=W, **paddings)
 
# preview da cor de preenchimento selecionada
cor_preenchimento_preview = Canvas(frame, width=20, height=20, background='red',
                                    highlightthickness=1, highlightbackground='gray')
cor_preenchimento_preview.grid(column=5, row=0, sticky=W, **paddings)
 
# checkbox para ativar/desativar o preenchimento das novas figuras
checkbox_preencher = ttk.Checkbutton(frame, text='Preencher figura', variable=preencher_var)
checkbox_preencher.grid(column=6, row=0, sticky=W, **paddings)
# Area de desenho
canvas = Canvas(frame, bg='white', width=600, height=600)
canvas.grid(column=0, row=1, columnspan=2, sticky=W, **paddings)

frame.pack()
formas.cor_borda_atual = cor_borda_atual
formas.cor_preenchimento_atual = cor_preenchimento_atual
formas.preencher_var = preencher_var
formas.canvas = canvas
formas.tipo_figura_var = tipo_figura_var

# Eventos de mouse associados ao canvas - com seus callbacks
canvas.bind('<ButtonPress-1>', iniciar_figura_nova)
canvas.bind('<B1-Motion>', atualizar_figura_nova)
canvas.bind('<ButtonRelease-1>', incluir_figura_nova)

root.mainloop()
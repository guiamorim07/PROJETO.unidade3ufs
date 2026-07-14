# nova mudança: Bernardo e Guilherme finalizaram a atualização feita por Gustavo (responsável por  iniciar e avançar consideravelmente o código em POO) adicionando a opção 'Polígono'  ass: Bernardo e Guilherme

from tkinter import *
from tkinter import ttk
from tkinter import colorchooser
import src.paint_ufs.formas as formas
from src.paint_ufs.formas import (iniciar_figura_nova, 
                    atualizar_figura_nova, 
                    incluir_figura_nova, 
                    mover_mouse, 
                    finalizar_poligono)
# ponto de entrada, criaremos a janela e chamaremos as funcoes


root = Tk()
root.title("Paint")
root.geometry("800x700")

frame = Frame(root)
frame.pack(fill=BOTH, expand=True)

# Widgets arranjados com Layout grid dentro de frame
paddings = {'padx': 5, 'pady': 5} 

toolbar = Frame(frame)
toolbar.grid(column=0, row=0, sticky=(W, E), **paddings)

# label
label = ttk.Label(toolbar,  text='Paint:')
label.grid(column=0, row=0, sticky=W, **paddings)

# option menu
tipo_figura_var = StringVar(root) # Guarda o tipo de figura selecionado no option menu
option_menu = ttk.OptionMenu(
    toolbar, tipo_figura_var,
                             'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo','Poligono')
option_menu.grid(column=1, row=0, sticky=W, **paddings)

ttk.Separator(toolbar, orient=VERTICAL).grid(column=2, row=0, sticky='ns', padx=10)

cor_borda_atual = StringVar(root, value='black')
 
# cor de preenchimento usada para desenhar novas figuras (retangulo, oval, circulo)
cor_preenchimento_atual = StringVar(root, value='red')
 
# controla se o preenchimento deve ser aplicado às novas figuras
preencher_var = BooleanVar(root, value=False)
 
 

# abre o seletor de cor do sistema e guarda a cor de borda escolhida
def escolher_cor_borda():
    cor = colorchooser.askcolor(title="Escolha a cor da borda")[1]  # [1] retorna o valor em hexadecimal
    if cor:
        cor_borda_atual.set(cor)
        cor_borda_preview.config(background=cor)
 
 

# abre o seletor de cor do sistema e guarda a cor de preenchimento escolhida
def escolher_cor_preenchimento():
    cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
    if cor:
        cor_preenchimento_atual.set(cor)
        cor_preenchimento_preview.config(background=cor)
 
 

# botão de escolher cor da borda
botao_cor_borda = ttk.Button(toolbar, text='Cor da borda', command=escolher_cor_borda)
botao_cor_borda.grid(column=3, row=0, sticky=W, **paddings)
 
# preview da cor de borda selecionada
cor_borda_preview = Canvas(toolbar, width=20, height=20, background='black',
                            highlightthickness=1, highlightbackground='gray')
cor_borda_preview.grid(column=4, row=0, sticky=W, **paddings)
 
# botão de escolher cor de preenchimento
botao_cor_preenchimento = ttk.Button(toolbar, text='Cor de preenchimento', command=escolher_cor_preenchimento)
botao_cor_preenchimento.grid(column=5, row=0, sticky=W, **paddings)
 
# preview da cor de preenchimento selecionada
cor_preenchimento_preview = Canvas(toolbar, width=20, height=20, background='red',
                                    highlightthickness=1, highlightbackground='gray')
cor_preenchimento_preview.grid(column=6, row=0, sticky=W, **paddings)
 
# checkbox para ativar/desativar o preenchimento das novas figuras
checkbox_preencher = ttk.Checkbutton(toolbar, text='Preencher figura', variable=preencher_var)
checkbox_preencher.grid(column=7, row=0, sticky=W, **paddings)

dica_poligono = ttk.Label(
    frame,
    text='Polígono: clique para adicionar vértices, duplo-clique (ou botão direito) para fechar.'
)
dica_poligono.grid(column=0, row=1, sticky=W, **paddings)

# Area de desenho
canvas = Canvas(frame, bg='white')
canvas.grid(column=0, row=2,  sticky=(N, S, E, W), **paddings)

frame.grid_columnconfigure(0, weight=1)
frame.grid_rowconfigure(2, weight=1)

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

canvas.bind('<Motion>', mover_mouse)                  # prévia do próximo segmento
canvas.bind('<Double-Button-1>', finalizar_poligono)  # fecha o polígono
canvas.bind('<Button-3>', finalizar_poligono)         # clique direito também fecha
root.mainloop()
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser

class PaintView:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint")
        self.root.geometry("800x700")

        self.frame = Frame(root)
        self.frame.pack(fill=BOTH, expand=True)

        paddings = {'padx': 5, 'pady': 5}

        self.toolbar = Frame(self.frame)
        self.toolbar.grid(column=0, row=0, sticky=(W, E), **paddings)

        ttk.Label(self.toolbar, text='Paint:').grid(column=0, row=0, sticky=W, **paddings)

        self.tipo_figura_var = StringVar(root)
        self.option_menu = ttk.OptionMenu(
            self.toolbar, self.tipo_figura_var,
            'Linha', 'Linha', 'Rabisco', 'Retangulo', 'Oval', 'Circulo', 'Poligono')
        self.option_menu.grid(column=1, row=0, sticky=W, **paddings)

        ttk.Separator(self.toolbar, orient=VERTICAL).grid(column=2, row=0, sticky='ns', padx=10)

        self.cor_borda_atual = StringVar(root, value='black')
        self.cor_preenchimento_atual = StringVar(root, value='red')
        self.preencher_var = BooleanVar(root, value=False)

        ttk.Button(self.toolbar, text='Cor da borda',
                   command=self._escolher_cor_borda).grid(column=3, row=0, sticky=W, **paddings)

        self.cor_borda_preview = Canvas(self.toolbar, width=20, height=20, background='black',
                                         highlightthickness=1, highlightbackground='gray')
        self.cor_borda_preview.grid(column=4, row=0, sticky=W, **paddings)

        ttk.Button(self.toolbar, text='Cor de preenchimento',
                   command=self._escolher_cor_preenchimento).grid(column=5, row=0, sticky=W, **paddings)

        self.cor_preenchimento_preview = Canvas(self.toolbar, width=20, height=20, background='red',
                                                 highlightthickness=1, highlightbackground='gray')
        self.cor_preenchimento_preview.grid(column=6, row=0, sticky=W, **paddings)

        ttk.Checkbutton(self.toolbar, text='Preencher figura',
                         variable=self.preencher_var).grid(column=7, row=0, sticky=W, **paddings)

        ttk.Label(
            self.frame,
            text='Polígono: clique para adicionar vértices, duplo-clique (ou botão direito) para fechar.'
        ).grid(column=0, row=1, sticky=W, **paddings)

        self.canvas = Canvas(self.frame, bg='white')
        self.canvas.grid(column=0, row=2, sticky=(N, S, E, W), **paddings)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(2, weight=1)

    # leitura do estado escolhido pelo usuário (o Controller vai chamar)

    def obter_tipo_figura(self):
        return self.tipo_figura_var.get()

    def obter_cor_borda(self):
        return self.cor_borda_atual.get()

    def obter_cor_preenchimento(self):
        if self.preencher_var.get():
            return self.cor_preenchimento_atual.get()
        return ''

    # desenho (o Controller manda desenhar, a View executa)

    def limpar_canvas(self):
        self.canvas.delete("all")

    def desenhar_figura(self, figura, preview=False):
        figura.desenhar(self.canvas, preview=preview)

    # registro de eventos: a View expõe o canvas, quem faz o bind é o Controller

    def bind_canvas(self, evento, callback):
        self.canvas.bind(evento, callback)

    # seletores de cor (comportamento visual puro, sem regra de negócio)

    def _escolher_cor_borda(self):
        cor = colorchooser.askcolor(title="Escolha a cor da borda")[1]
        if cor:
            self.cor_borda_atual.set(cor)
            self.cor_borda_preview.config(background=cor)

    def _escolher_cor_preenchimento(self):
        cor = colorchooser.askcolor(title="Escolha a cor de preenchimento")[1]
        if cor:
            self.cor_preenchimento_atual.set(cor)
            self.cor_preenchimento_preview.config(background=cor)
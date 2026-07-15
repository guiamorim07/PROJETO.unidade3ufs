

from tkinter import Tk
from src.paint_ufs.View.view import PaintView
from src.paint_ufs.Controller.formas import Controller

root = Tk()
view = PaintView(root)
Controller = Controller(view)

root.mainloop()
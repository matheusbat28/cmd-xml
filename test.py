from tkinter import Tk
from tkinter.filedialog import askopenfilename, asksaveasfile
import time
import os

Tk().withdraw()

arq = None
arquivo = askopenfilename(filetypes=(("Text files", "*.xml"),))

print(arquivo)      


import tkinter as tk
from PIL import ImageTk, Image
from asa import *
from posto import *
from dxd import *
from comandos_teste import teste
from janela_mae import *
from DGs.ilhaProibida import ilhaProibida
from DGs.altarSiena1SS import altarSiena1SS
from DGs.castelo_das_ilusoes import castelo_das_ilusoes
from DGs.salao_radiante_do_castelo_das_ilusoes import salao_radiante_do_castelo_das_ilusoes
from DGs.b1f import b1f
from DGs.b2f import b2f
from DGs.crista import crista

def botao_crista():
    crista(bp_var.get(),  mula_var.get())

janela_2 = tk.Toplevel(janela)
janela_2.geometry("300x600+850+50")  # Definir a posição da janela_1
janela_2.title("DGs 2")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
mula_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela_2, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela_2, text="BP", variable=bp_var)
mula = tk.Checkbutton(janela_2, text="mula", variable=mula_var)

# Abrir a imagem a ser usada no botão
imgcrista = Image.open(caminho + "\\imgs\\botoes\\cristaIlusoria.png")
imgcrista = imgcrista.resize((100, 100)) # definir o tamanho da imagem
imgcrista = ImageTk.PhotoImage(imgcrista)

# Criar o botão
btn_chave1 = tk.Button(janela_2, image=imgcrista, command=botao_crista)
btn_chave1.image = imgcrista # Salvar a referência da imagem para evitar o garbage collection
btn_chave1.grid(row=6, column=0)

btn_teste = tk.Button(janela_2, command=teste)
btn_teste.grid(row=10, column=1)

# Adicionar as checkboxes à janela_1
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
mula.grid(row=1, column=0)


janela_2.withdraw()

     
def janela_2_esconder():
    janela_2.withdraw()
    
def janela_2_mostrar():
    janela_2.deiconify()

def janela_2_fechar(func):
  janela_2.protocol("WM_DELETE_WINDOW", func)

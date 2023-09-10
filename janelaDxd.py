import tkinter as tk
from PIL import ImageTk, Image
from asa import *
from posto import *
from dxd import *
from comandos_teste import teste
from janela_mae import *
from DGs.DX.morada_das_chamas_desperto import morada_desperta
from DGs.DXD.locomotivaLouca import locomotivaLoucaDesperta

def botao_locomotiva_louca_desperta():
    locomotivaLoucaDesperta(bp_var.get(), mula_var.get())

def botao_posto():
    posto(gemas_var.get(), bp_var.get(), mula_var.get())

def botao_vale_desperto():
    vale_desperto(bp_var.get(),  mula_var.get())

def botao_morada_desperta():
    morada_desperta(bp_var.get(),  mula_var.get())

def botao_catacumba_desperta():
    catacumba_desperta(bp_var.get(),  mula_var.get())

janela_dxd = tk.Toplevel(janela)
janela_dxd.geometry("300x600+850+50")  # Definir a posição da janela_dxd
janela_dxd.title("DXD")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
mula_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela_dxd, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela_dxd, text="BP", variable=bp_var)
mula = tk.Checkbutton(janela_dxd, text="mula", variable=mula_var)

# Abrir a imagem a ser usada no botão
imglocomotiva_louca_desperta = Image.open(caminho + "\\imgs\\botoes\\trem_d.png")
imglocomotiva_louca_desperta = imglocomotiva_louca_desperta.resize((100, 100)) # definir o tamanho da imagem
imglocomotiva_louca_desperta = ImageTk.PhotoImage(imglocomotiva_louca_desperta)

imgposto = Image.open(caminho + "\\imgs\\botoes\\posto.png")
imgposto = imgposto.resize((100, 100)) # definir o tamanho da imagem
imgposto = ImageTk.PhotoImage(imgposto)

img_vale_desperto = Image.open(caminho + "\\imgs\\botoes\\ovo_d.png")
img_vale_desperto = img_vale_desperto.resize((100, 100)) # definir o tamanho da imagem
img_vale_desperto = ImageTk.PhotoImage(img_vale_desperto)

img_morada_desperta = Image.open(caminho + "\\imgs\\botoes\\morada_desperta.png")
img_morada_desperta = img_morada_desperta.resize((100, 100)) # definir o tamanho da imagem
img_morada_desperta = ImageTk.PhotoImage(img_morada_desperta)

img_catacumba_desperta = Image.open(caminho + "\\imgs\\botoes\\catacumba_desperta.png")
img_catacumba_desperta = img_catacumba_desperta.resize((100, 100)) # definir o tamanho da imagem
img_catacumba_desperta = ImageTk.PhotoImage(img_catacumba_desperta)

# Criar o botão
btn_chave1 = tk.Button(janela_dxd, image=imglocomotiva_louca_desperta, command=botao_locomotiva_louca_desperta)
btn_chave1.image = imglocomotiva_louca_desperta # Salvar a referência da imagem para evitar o garbage collection
btn_chave1.grid(row=6, column=0)

btn_chave2 = tk.Button(janela_dxd, image=imgposto, command=botao_posto)
btn_chave2.image = imgposto # Salvar a referência da imagem para evitar o garbage collection
btn_chave2.grid(row=6, column=1)

btn_vale_desperto = tk.Button(janela_dxd, image=img_vale_desperto, command=botao_vale_desperto)
btn_vale_desperto.image = img_vale_desperto # Salvar a referência da imagem para evitar o garbage collection
btn_vale_desperto.grid(row=7, column=0)

btn_morada_desperta = tk.Button(janela_dxd, image=img_morada_desperta, command=botao_morada_desperta)
btn_morada_desperta.image = img_morada_desperta # Salvar a referência da imagem para evitar o garbage collection
btn_morada_desperta.grid(row=7, column=1)

btn_catacumba_desperta = tk.Button(janela_dxd, image=img_catacumba_desperta, command=botao_catacumba_desperta)
btn_catacumba_desperta.image = img_catacumba_desperta # Salvar a referência da imagem para evitar o garbage collection
btn_catacumba_desperta.grid(row=8, column=0)


btn_teste = tk.Button(janela_dxd, command=teste)
btn_teste.grid(row=9, column=1)

# Adicionar as checkboxes à janela_dxd
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
mula.grid(row=1, column=0)


janela_dxd.withdraw()

     
def janela_dxd_esconder():
    janela_dxd.withdraw()
    
def janela_dxd_mostrar():
    janela_dxd.deiconify()

def janela_dxd_fechar(func):
  janela_dxd.protocol("WM_DELETE_WINDOW", func)

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
from DGs.b1f import b1f

def botao_moinho():
    chave(bp_var.get(), mula_var.get())

def botao_posto():
    posto(gemas_var.get(), bp_var.get(), mula_var.get())

def botao_castelo_das_ilusoes():
    castelo_das_ilusoes(gemas_var.get(), bp_var.get(),  mula_var.get())

def botao_b1f():
    b1f(gemas_var.get(), bp_var.get(),  mula_var.get())

def botao_ilhaProibida():
    ilhaProibida(bp_var.get(),  mula_var.get())

def botao_altarSiena1SS():
    altarSiena1SS(bp_var.get(),  mula_var.get())

janela_1 = tk.Toplevel(janela)
janela_1.geometry("300x600+850+50")  # Definir a posição da janela_1
janela_1.title("DGs 1")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
mula_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela_1, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela_1, text="BP", variable=bp_var)
mula = tk.Checkbutton(janela_1, text="mula", variable=mula_var)

# Abrir a imagem a ser usada no botão
imgmoinho = Image.open(caminho + "\\imgs\\botoes\\moinho.png")
imgmoinho = imgmoinho.resize((100, 100)) # definir o tamanho da imagem
imgmoinho = ImageTk.PhotoImage(imgmoinho)

imgposto = Image.open(caminho + "\\imgs\\botoes\\posto.png")
imgposto = imgposto.resize((100, 100)) # definir o tamanho da imagem
imgposto = ImageTk.PhotoImage(imgposto)

img_castelo_das_ilusoes = Image.open(caminho + "\\imgs\\botoes\\copia_apocalipse_ilusivo.png")
img_castelo_das_ilusoes = img_castelo_das_ilusoes.resize((100, 100)) # definir o tamanho da imagem
img_castelo_das_ilusoes = ImageTk.PhotoImage(img_castelo_das_ilusoes)

img_b1f = Image.open(caminho + "\\imgs\\botoes\\dragonaDosMortos.png")
img_b1f = img_b1f.resize((100, 100)) # definir o tamanho da imagem
img_b1f = ImageTk.PhotoImage(img_b1f)

imgilhaProibida = Image.open(caminho + "\\imgs\\botoes\\BussulaIlhaProibida.png")
imgilhaProibida = imgilhaProibida.resize((100, 100)) # definir o tamanho da imagem
imgilhaProibida = ImageTk.PhotoImage(imgilhaProibida)

imgAltarSiena1SS = Image.open(caminho + "\\imgs\\botoes\\s1.png")
imgAltarSiena1SS = imgAltarSiena1SS.resize((100, 100)) # definir o tamanho da imagem
imgAltarSiena1SS = ImageTk.PhotoImage(imgAltarSiena1SS)

# Criar o botão
btn_chave1 = tk.Button(janela_1, image=imgmoinho, command=botao_moinho)
btn_chave1.image = imgmoinho # Salvar a referência da imagem para evitar o garbage collection
btn_chave1.grid(row=6, column=0)

btn_chave2 = tk.Button(janela_1, image=imgposto, command=botao_posto)
btn_chave2.image = imgposto # Salvar a referência da imagem para evitar o garbage collection
btn_chave2.grid(row=6, column=1)

btn_castelo_das_ilusoes = tk.Button(janela_1, image=img_castelo_das_ilusoes, command=botao_castelo_das_ilusoes)
btn_castelo_das_ilusoes.image = img_castelo_das_ilusoes # Salvar a referência da imagem para evitar o garbage collection
btn_castelo_das_ilusoes.grid(row=7, column=0)

btn_b1f = tk.Button(janela_1, image=img_b1f, command=botao_b1f)
btn_b1f.image = img_b1f # Salvar a referência da imagem para evitar o garbage collection
btn_b1f.grid(row=7, column=1)

btn_ilhaProibida = tk.Button(janela_1, image=imgilhaProibida, command=botao_ilhaProibida)
btn_ilhaProibida.image = imgilhaProibida # Salvar a referência da imagem para evitar o garbage collection
btn_ilhaProibida.grid(row=8, column=0)

btn_altarSiena1SS = tk.Button(janela_1, image=imgAltarSiena1SS, command=botao_altarSiena1SS)
btn_altarSiena1SS.image = imgAltarSiena1SS # Salvar a referência da imagem para evitar o garbage collection
btn_altarSiena1SS.grid(row=8, column=1)


btn_teste = tk.Button(janela_1, command=teste)
btn_teste.grid(row=9, column=1)

# Adicionar as checkboxes à janela_1
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
mula.grid(row=1, column=0)


janela_1.withdraw()

     
def janela_1_esconder():
    janela_1.withdraw()
    
def janela_1_mostrar():
    janela_1.deiconify()

def janela_1_fechar(func):
  janela_1.protocol("WM_DELETE_WINDOW", func)

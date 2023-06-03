import tkinter as tk
from PIL import ImageTk, Image
from asa import *
from posto import *
from dxd import *
from comandos_teste import teste
from janela_mae import *
from DGs.DX.morada_das_chamas_desperto import  morada_das_chamas
from DGs.DX.caverda_do_panico import caverna_do_panico
from DGs.DX.locomotivaLouca import locomotivaLouca
from DGs.DX.catacumbaGelida import catacumbaGelida


def botao_morada_das_chamas():
    morada_das_chamas(bp_var.get(),  mula_var.get(), escolha.get() )

def botao_catacumbaGelida():
    catacumbaGelida(bp_var.get(),  mula_var.get(), escolha.get())

def botao_caverna_do_panico():
    caverna_do_panico(bp_var.get(),  mula_var.get(), escolha.get())

def botao_locomotivaLouca():
    locomotivaLouca(bp_var.get(),  mula_var.get(), escolha.get())

janela_dx = tk.Toplevel(janela)
janela_dx.geometry("300x600+850+50")  # Definir a posição da janela_dx
janela_dx.title("DX")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
mula_var = tk.BooleanVar()
escolha = tk.StringVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela_dx, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela_dx, text="BP", variable=bp_var)
mula = tk.Checkbutton(janela_dx, text="mula", variable=mula_var)
rb_facil = tk.Radiobutton(janela_dx, text="Fácil", variable=escolha, value="facil")
rb_medio = tk.Radiobutton(janela_dx, text="Médio", variable=escolha, value="medio")
rb_dificil = tk.Radiobutton(janela_dx, text="Difícil", variable=escolha, value="dificil")
rb_premium = tk.Radiobutton(janela_dx, text="Premium", variable=escolha, value="premium")
rb_elite = tk.Radiobutton(janela_dx, text="Elite", variable=escolha, value="elite")


# Abrir a imagem a ser usada no botão
img_morada_das_chamas = Image.open(caminho + "\\imgs\\botoes\\lava_premium.png")
img_morada_das_chamas = img_morada_das_chamas.resize((100, 100)) # definir o tamanho da imagem
img_morada_das_chamas = ImageTk.PhotoImage(img_morada_das_chamas)

img_catacumbaGelida = Image.open(caminho + "\\imgs\\botoes\\novo_vestigio_congelado.png")
img_catacumbaGelida = img_catacumbaGelida.resize((100, 100)) # definir o tamanho da imagem
img_catacumbaGelida = ImageTk.PhotoImage(img_catacumbaGelida)

img_caverna_do_panico = Image.open(caminho + "\\imgs\\botoes\\diario_premium.png")
img_caverna_do_panico = img_caverna_do_panico.resize((100, 100)) # definir o tamanho da imagem
img_caverna_do_panico = ImageTk.PhotoImage(img_caverna_do_panico)

img_locomotivaLouca = Image.open(caminho + "\\imgs\\botoes\\cartao_trem_premium.png")
img_locomotivaLouca = img_locomotivaLouca.resize((100, 100)) # definir o tamanho da imagem
img_locomotivaLouca = ImageTk.PhotoImage(img_locomotivaLouca)

# Criar o botão
btn_locomotivaLouca = tk.Button(janela_dx, image=img_locomotivaLouca, command=botao_locomotivaLouca)
btn_locomotivaLouca.image = img_locomotivaLouca # Salvar a referência da imagem para evitar o garbage collection
btn_locomotivaLouca.grid(row=7, column=0)

btn_morada_das_chamas = tk.Button(janela_dx, image=img_morada_das_chamas, command=botao_morada_das_chamas)
btn_morada_das_chamas.image = img_morada_das_chamas # Salvar a referência da imagem para evitar o garbage collection
btn_morada_das_chamas.grid(row=7, column=1)

btn_catacumbaGelida = tk.Button(janela_dx, image=img_catacumbaGelida, command=botao_catacumbaGelida)
btn_catacumbaGelida.image = img_catacumbaGelida # Salvar a referência da imagem para evitar o garbage collection
btn_catacumbaGelida.grid(row=8, column=0)

btn_caverna_do_panico = tk.Button(janela_dx, image=img_caverna_do_panico, command=botao_caverna_do_panico)
btn_caverna_do_panico.image = img_caverna_do_panico # Salvar a referência da imagem para evitar o garbage collection
btn_caverna_do_panico.grid(row=8, column=1)

btn_teste = tk.Button(janela_dx, command=teste)
btn_teste.grid(row=9, column=1)

# Adicionar as checkboxes à janela_dx
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
mula.grid(row=1, column=0)
rb_facil.grid(row=2, column=0)
rb_medio.grid(row=2, column=1)
rb_dificil.grid(row=3, column=2)
rb_premium.grid(row=3, column=0)
rb_elite.grid(row=3, column=1)


janela_dx.withdraw()

def janela_dx_esconder():
    janela_dx.withdraw()
    
def janela_dx_mostrar():
    janela_dx.deiconify()

def janela_dx_fechar(func):
  janela_dx.protocol("WM_DELETE_WINDOW", func)
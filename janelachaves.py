import tkinter as tk
from PIL import ImageTk, Image
from chave import *
from comandos_teste import teste
from arena_do_eterno import *
from janela_mae import *
    
def botao_chave1():
    chave(dg1, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave2():
    chave(dg2, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave3():
    chave(dg3, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave4():
    chave(dg4, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave5():
    chave(dg5, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave6():
    chave(dg6, gemas_var.get(), bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_chave7():
    chave(dg7, False, bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_rush():
    chave(bp_var.get(), esperar_var.get(), mula_var.get(), bm_var.get())

def botao_arena_eterno():
    arena_eterno(gemas_var.get(), bp_var.get(), mula_var.get())


janela_chave = tk.Toplevel(janela)
janela_chave.geometry("300x700+850+50")  # Definir a posição da janela
janela_chave.title("Chaves do Caos")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
mula_var = tk.BooleanVar()
esperar_var = tk.BooleanVar()
bm_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela_chave, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela_chave, text="usar BP", variable=bp_var)
mula = tk.Checkbutton(janela_chave, text="mula", variable=mula_var)
esperar = tk.Checkbutton(janela_chave, text="Esperar tempo", variable=esperar_var)
bm = tk.Checkbutton(janela_chave, text="matar boss de bm3", variable=bm_var)

# Abrir a imagem a ser usada no botão
imgchave1 = Image.open(caminho + "\\imgs\\botoes\\chave1.png")
imgchave1 = imgchave1.resize((100, 100)) # definir o tamanho da imagem
imgchave1 = ImageTk.PhotoImage(imgchave1)

imgchave2 = Image.open(caminho + "\\imgs\\botoes\\chave2.png")
imgchave2 = imgchave2.resize((100, 100)) # definir o tamanho da imagem
imgchave2 = ImageTk.PhotoImage(imgchave2)

imgchave3 = Image.open(caminho + "\\imgs\\botoes\\chave3.png")
imgchave3 = imgchave3.resize((100, 100)) # definir o tamanho da imagem
imgchave3 = ImageTk.PhotoImage(imgchave3)

imgchave4 = Image.open(caminho + "\\imgs\\botoes\\chave4.png")
imgchave4 = imgchave4.resize((100, 100)) # definir o tamanho da imagem
imgchave4 = ImageTk.PhotoImage(imgchave4)

imgchave5 = Image.open(caminho + "\\imgs\\botoes\\chave5.png")
imgchave5 = imgchave5.resize((100, 100)) # definir o tamanho da imagem
imgchave5 = ImageTk.PhotoImage(imgchave5)

imgchave6 = Image.open(caminho + "\\imgs\\botoes\\chave6.png")
imgchave6 = imgchave6.resize((100, 100)) # definir o tamanho da imagem
imgchave6 = ImageTk.PhotoImage(imgchave6)

imgchave7 = Image.open(caminho + "\\imgs\\botoes\\chave7.png")
imgchave7 = imgchave7.resize((100, 100)) # definir o tamanho da imagem
imgchave7 = ImageTk.PhotoImage(imgchave7)

imgrush = Image.open(caminho + "\\imgs\\botoes\\rush.png")
imgrush = imgrush.resize((100, 100)) # definir o tamanho da imagem
imgrush = ImageTk.PhotoImage(imgrush)

imgchave_eterno = Image.open(caminho + "\\imgs\\botoes\\chave_eterno.png")
imgchave_eterno = imgchave_eterno.resize((100, 100)) # definir o tamanho da imagem
imgchave_eterno = ImageTk.PhotoImage(imgchave_eterno)


# Criar o botão
btn_chave1 = tk.Button(janela_chave, image=imgchave1, command=botao_chave1)
btn_chave1.image = imgchave1 # Salvar a referência da imagem para evitar o garbage collection
btn_chave1.grid(row=6, column=0)

btn_chave2 = tk.Button(janela_chave, image=imgchave2, command=botao_chave2)
btn_chave2.image = imgchave2 # Salvar a referência da imagem para evitar o garbage collection
btn_chave2.grid(row=6, column=1)

btn_chave3 = tk.Button(janela_chave, image=imgchave3, command=botao_chave3)
btn_chave3.image = imgchave3 # Salvar a referência da imagem para evitar o garbage collection
btn_chave3.grid(row=7, column=0)

btn_chave4 = tk.Button(janela_chave, image=imgchave4, command=botao_chave4)
btn_chave4.image = imgchave4 # Salvar a referência da imagem para evitar o garbage collection
btn_chave4.grid(row=7, column=1)

btn_chave5 = tk.Button(janela_chave, image=imgchave5, command=botao_chave5)
btn_chave5.image = imgchave5 # Salvar a referência da imagem para evitar o garbage collection
btn_chave5.grid(row=8, column=0)

btn_chave6 = tk.Button(janela_chave, image=imgchave6, command=botao_chave6)
btn_chave6.image = imgchave6 # Salvar a referência da imagem para evitar o garbage collection
btn_chave6.grid(row=8, column=1)

btn_chave7 = tk.Button(janela_chave, image=imgchave7, command=botao_chave7)
btn_chave7.image = imgchave7 # Salvar a referência da imagem para evitar o garbage collection
btn_chave7.grid(row=9, column=0)

btn_rush = tk.Button(janela_chave, image=imgrush, command=botao_rush)
btn_rush.image = imgrush # Salvar a referência da imagem para evitar o garbage collection
btn_rush.grid(row=9, column=1)

btn_chave_eterno = tk.Button(janela_chave, image=imgchave_eterno, command=botao_arena_eterno)
btn_chave_eterno.image = imgchave_eterno # Salvar a referência da imagem para evitar o garbage collection
btn_chave_eterno.grid(row=10, column=0)

btn_teste = tk.Button(janela_chave, command=teste)
btn_teste.grid(row=10, column=1)


# Adicionar as checkboxes à janela
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
mula.grid(row=1, column=0)
esperar.grid(row=1, column=1)
bm.grid(row=2, column=0)

    
janela_chave.withdraw()

def janela_chaves_esconder():
    janela_chave.withdraw()
    
def janela_chaves_mostrar():
    janela_chave.deiconify()

def janela_chave_fechar(func):
  janela_chave.protocol("WM_DELETE_WINDOW", func)


import tkinter as tk
from PIL import ImageTk, Image
from chave import *

def botao_chave1():
    chave(chave1, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave2():
    chave(chave2, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave3():
    chave(chave3, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave4():
    chave(chave4, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave5():
    chave(chave5, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave6():
    chave(chave6, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_chave7():
    chave(chave7, gemas_var.get(), bp_var.get(), revive_var.get())

janela = tk.Tk()
janela.geometry("300x600+850+50")  # Definir a posição da janela
janela.title("nome")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
revive_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela, text="BP", variable=bp_var)
revive_cb = tk.Checkbutton(janela, text="Revive", variable=revive_var)

# Abrir a imagem a ser usada no botão
imgchave1 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave1.png")
imgchave1 = imgchave1.resize((100, 100)) # definir o tamanho da imagem
imgchave1 = ImageTk.PhotoImage(imgchave1)

imgchave2 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave2.png")
imgchave2 = imgchave2.resize((100, 100)) # definir o tamanho da imagem
imgchave2 = ImageTk.PhotoImage(imgchave2)

imgchave3 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave3.png")
imgchave3 = imgchave3.resize((100, 100)) # definir o tamanho da imagem
imgchave3 = ImageTk.PhotoImage(imgchave3)

imgchave4 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave4.png")
imgchave4 = imgchave4.resize((100, 100)) # definir o tamanho da imagem
imgchave4 = ImageTk.PhotoImage(imgchave4)

imgchave5 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave5.png")
imgchave5 = imgchave5.resize((100, 100)) # definir o tamanho da imagem
imgchave5 = ImageTk.PhotoImage(imgchave5)

imgchave6 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave6.png")
imgchave6 = imgchave6.resize((100, 100)) # definir o tamanho da imagem
imgchave6 = ImageTk.PhotoImage(imgchave6)

imgchave7 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\botoes\\chave7.png")
imgchave7 = imgchave7.resize((100, 100)) # definir o tamanho da imagem
imgchave7 = ImageTk.PhotoImage(imgchave7)


# Criar o botão
btn_chave1 = tk.Button(janela, image=imgchave1, command=botao_chave1)
btn_chave1.image = imgchave1 # Salvar a referência da imagem para evitar o garbage collection
btn_chave1.grid(row=1, column=0)

btn_chave2 = tk.Button(janela, image=imgchave2, command=botao_chave2)
btn_chave2.image = imgchave2 # Salvar a referência da imagem para evitar o garbage collection
btn_chave2.grid(row=1, column=1)

btn_chave3 = tk.Button(janela, image=imgchave3, command=botao_chave3)
btn_chave3.image = imgchave3 # Salvar a referência da imagem para evitar o garbage collection
btn_chave3.grid(row=2, column=0)

btn_chave4 = tk.Button(janela, image=imgchave4, command=botao_chave4)
btn_chave4.image = imgchave4 # Salvar a referência da imagem para evitar o garbage collection
btn_chave4.grid(row=2, column=1)

btn_chave5 = tk.Button(janela, image=imgchave5, command=botao_chave5)
btn_chave5.image = imgchave5 # Salvar a referência da imagem para evitar o garbage collection
btn_chave5.grid(row=3, column=0)

btn_chave6 = tk.Button(janela, image=imgchave6, command=botao_chave6)
btn_chave6.image = imgchave6 # Salvar a referência da imagem para evitar o garbage collection
btn_chave6.grid(row=3, column=1)

btn_chave7 = tk.Button(janela, image=imgchave7, command=botao_chave7)
btn_chave7.image = imgchave7 # Salvar a referência da imagem para evitar o garbage collection
btn_chave7.grid(row=4, column=0)

# Adicionar as checkboxes à janela
gemas_cb.grid(row=0, column=0)
bp_cb.grid(row=0, column=1)
revive_cb.grid(row=0, column=2)

janela.mainloop()

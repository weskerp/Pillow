import tkinter as tk
from PIL import ImageTk, Image
from chave import chave, chave1, chave2

def botao_clicado():
    chave(chave1, gemas_var.get(), bp_var.get(), revive_var.get())

def botao_clicado2():
    chave(chave2, gemas_var.get(), bp_var.get(), revive_var.get())

janela = tk.Tk()
janela.geometry("300x600")
janela.title("Exemplo de botão")

# Criar as variáveis das checkboxes
gemas_var = tk.BooleanVar()
bp_var = tk.BooleanVar()
revive_var = tk.BooleanVar()

# Criar as checkboxes
gemas_cb = tk.Checkbutton(janela, text="Gemas", variable=gemas_var)
bp_cb = tk.Checkbutton(janela, text="BP", variable=bp_var)
revive_cb = tk.Checkbutton(janela, text="Revive", variable=revive_var)

# Abrir a imagem a ser usada no botão
imagem = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\800x600\\BMMA.png")
imagem = imagem.resize((100, 100)) # definir o tamanho da imagem
imagem = ImageTk.PhotoImage(imagem)

imagem2 = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\800x600\\IT8.png")
imagem2 = imagem2.resize((100, 100)) # definir o tamanho da imagem
imagem2 = ImageTk.PhotoImage(imagem2)

# Criar o botão
botao = tk.Button(janela, image=imagem, command=botao_clicado)
botao.image = imagem # Salvar a referência da imagem para evitar o garbage collection
botao.pack(side=tk.LEFT)


botao2 = tk.Button(janela, image=imagem2, command=botao_clicado2)
botao2.image = imagem2 # Salvar a referência da imagem para evitar o garbage collection
botao2.pack(side=tk.RIGHT)

# Adicionar as checkboxes à janela
gemas_cb.pack()
bp_cb.pack()
revive_cb.pack()

janela.mainloop()

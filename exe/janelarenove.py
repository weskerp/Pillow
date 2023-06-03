import tkinter as tk


def janela_msg_pagamento():
    janela = tk.Tk()
    janela.geometry("400x100+850+250")  # Definir a posição da janela
    janela.title("ERROR")

    texto = "Renove a mensalidade para continuar usando"
    label = tk.Label(janela, text=texto)
    label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    janela.mainloop()
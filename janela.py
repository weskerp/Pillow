import tkinter as tk
from janelachaves import janela_chaves_esconder, janela_chaves_mostrar, janela_chave_fechar
from janelaDxd import janela_dxd_mostrar, janela_dxd_esconder, janela_dxd_fechar
from janela1 import janela_1_mostrar, janela_1_esconder, janela_1_fechar
from janela2 import janela_2_mostrar, janela_2_esconder, janela_2_fechar
from janelaDX import janela_dx_mostrar, janela_dx_esconder, janela_dx_fechar
from janela_mae import *
from up_sn_capella import up_sn
from map import mapear

def janela_botoes():
    def abrir_janela_chave():
        janela.withdraw()
        janela_chaves_mostrar()
        janela_chave_fechar(fechar_janela_chave)

    def fechar_janela_chave():
        janela_chaves_esconder()
        janela.deiconify()

    def abrir_janela_dxd():
        janela.withdraw()
        janela_dxd_mostrar()
        janela_dxd_fechar(fechar_janela_dxd)

    def fechar_janela_dxd():
        janela_dxd_esconder()
        janela.deiconify()
    
    def abrir_janela_dx():
        janela.withdraw()
        janela_dx_mostrar()
        janela_dx_fechar(fechar_janela_dx)

    def fechar_janela_dx():
        janela_dx_esconder()
        janela.deiconify()
    
    def abrir_janela_1():
        janela.withdraw()
        janela_1_mostrar()
        janela_1_fechar(fechar_janela_1)

    def fechar_janela_1():
        janela_1_esconder()
        janela.deiconify()
    
    def abrir_janela_2():
        janela.withdraw()
        janela_2_mostrar()
        janela_2_fechar(fechar_janela_2)

    def fechar_janela_2():
        janela_2_esconder()
        janela.deiconify()

    def upSnCapella():
        up_sn()
        
    def upSnCapellaFantasmas():
        up_sn(fantasma = True)
    
    # Criar o botão
    btn_chave = tk.Button(janela, text="Chaves do Caos", command=abrir_janela_chave)
    btn_chave.grid(row=0, column=0)

    btn_dxd = tk.Button(janela, text="DXD", command=abrir_janela_dxd)
    btn_dxd.grid(row=0, column=1)
    
    btn_chave = tk.Button(janela, text="DX", command=abrir_janela_dx)
    btn_chave.grid(row=1, column=0)

    btn_dxd = tk.Button(janela, text="DGs 1", command=abrir_janela_1)
    btn_dxd.grid(row=1, column=1)
    
    btn_dxd = tk.Button(janela, text="DGs 1", command=abrir_janela_2)
    btn_dxd.grid(row=2, column=0)

    # Espaço vazio na linha
    empty_label = tk.Label(janela)
    empty_label.grid(row=4)

    empty_label2 = tk.Label(janela)
    empty_label2.grid(row=5)

    btnUpSn = tk.Button(janela, text="Upar em Sinelinea spot capella", bg="#66245b", command=upSnCapella)
    btnUpSn.grid(row=6,  columnspan=2)
    
    btnUpSn = tk.Button(janela, text="Upar em Sinelinea spot capella fantasmas", bg="#66245b", command=upSnCapellaFantasmas)
    btnUpSn.grid(row=7,  columnspan=2)
    
    def atualizar_label():
        # Atualiza o texto da label com a nova saída da função map()
        coord = mapear()
        label.config(text=coord)
        # Agendar a função para ser executada novamente após 5 segundos
        janela.after(50, atualizar_label)

    label = tk.Label(janela)
    label.grid(row=9, column=1)

# Chama a função para atualizar o texto da label pela primeira vez
    atualizar_label()
    
    janela.mainloop()

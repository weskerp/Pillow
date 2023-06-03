import pyautogui
import time
from comandos import *

def pandemonio(gema, bp, mula):
    inicio_pt1()
    inicio_pt2(184, 118)
    if tela_dg():
        dg3()
        time.sleep(0.2)
        pyautogui.moveTo(287, 165)
        time.sleep(1.6)
        # Verifica se a imagem alvo está presente na coordenada especificada
        while entrada_disponivel(gema):
            # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
            entrar(gema)
            start()
            usar_buff()
            


    
   
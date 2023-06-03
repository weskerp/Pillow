import pyautogui
import time
from PIL import Image
from comandos import *


boss = Image.open(caminho + "\\imgs\\boss.png")

def posto(gema, bp, mula):
    
    time.sleep(1)
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    preparacao()
    andar_esquerda_tras(1)
    pyautogui.moveTo(320, 222)
    time.sleep(2)
    pyautogui.click()
    dg1()
    time.sleep(1)
    # Verifica se a imagem alvo está presente na coordenada especificada
    if teste_entrar():
        # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
        entrar(False)
        start()
        usar_buff()
        andar_frente(1.8)
        time.sleep(1)
        pyautogui.moveTo(407, 303)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        keyboard.send('space')
        time.sleep(1)
        keyboard.send('space')
        andar_esquerda_frente(5)
        time.sleep(1)
        pyautogui.moveTo(30, 303)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        keyboard.send('space')
        andar_esquerda(1)
        keyboard.send('z')
        matar_boss('bm3')



    
   
import pyautogui
import time
from comandos import *
def caminho1():
    inicio_pt1()
    set_pausar_codigo_principal(False)
    time.sleep(0.5)
    keyboard.send('m')
    time.sleep(0.5)
    pyautogui.moveTo(423, 280)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(1)
    andar_direita_frente(5)
    andar_esquerda_frente(3)

def up_sn():
    global pausar_codigo_principal
    esta_vivo()
    while(True):
        caminho1()
        cont = 0
        while cont < 3000:
            atacar()
            recolher_alz()
            keyboard.send('z')
            cont = cont+1
            if pausar_principal():
                caminho1()
        keyboard.send('o')
        time.sleep(0.5)
        pyautogui.moveTo(389, 299)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(0.5)
        pyautogui.moveTo(404, 398)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(731, 607)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(5)
        pyautogui.moveTo(770, 596)
        time.sleep(0.5)
        pyautogui.click()
        time.sleep(6)
    global cancelar_esta_vivo
    cancelar_esta_vivo = True
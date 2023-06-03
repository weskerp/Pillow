import pyautogui
import time
from comandos import *



def matar_boss_vale_desperto():
    print("Entrar boss vale desperto")
    if pyautogui.locateOnScreen(sp_final) is not None: 
        ativar_bm3()
        for i in range(3):
            keyboard.send('z')
            while pyautogui.locateOnScreen(boss) is not None:
                atacar_bm3(sinergia1, False)
                if pyautogui.locateOnScreen(boss) is not None:
                    atacar_bm3(sinergia2, False)
                if pyautogui.locateOnScreen(boss) is not None:
                    atacar_bm3(sinergia3, False)
                if pyautogui.locateOnScreen(boss) is not None:
                    fatal(False)
        cancelar_bm()
    else:
        for i in range(3):
            keyboard.send('z')
            while pyautogui.locateOnScreen(boss) is not None:
                atacar()
                keyboard.send('z')
                keyboard.send('space')
    time.sleep(2)
    
    for i in range(3):
        quebrar_bau('bau')
    print("Sair boss vale desperto")

def boss1():
    print('entrar boss1')
    matar_monstro_ate_boss()
    matar_boss('bm3')
    quebrar_bau('bau')
    print('sair boss1')

def boss2():
    print('entrar boss2')
    matar_boss('bm3')
    quebrar_bau('bau')
    print('sair boss2')
    
def caminho1():
    print("entrar caminho1")
    if not tem_boss():
        andar_direita_tras(3)
        time.sleep(0.5)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(2)
    if not tem_boss():
        time.sleep(0.5)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(1)
    if not tem_boss():
        time.sleep(0.5)
        matar_monstros()
        time.sleep(0.5)
        andar_direita(3)
    if not tem_boss():
        andar_tras(0.8)
        andar_direita(2)
        andar_direita_tras(2)
    if not tem_boss():
        andar_tras(3.8)
        andar_direita_tras(17)
    print('sair caminho1')

def caminho2():
    print("Entrar caminho 2")
    if not tem_boss():
        andar_direita_tras(1.5)
        andar_tras(2)
        andar_direita(3)
    if not tem_boss():
        andar_direita(1)
        andar_direita_tras(1)
        andar_tras(2)
        andar_direita_tras(2)
    if not tem_boss():
        time.sleep(0.5)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(4)
    if not tem_boss():
        time.sleep(0.5)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(4)
    if not tem_boss():
        time.sleep(0.5)
        matar_monstros()
        andar_tras(1)
        andar_direita_tras(4)
    if not tem_boss():
        andar_direita(1)
        andar_direita_tras(8)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(4)
    if not tem_boss():
        andar_tras(2)
        matar_monstros()
        time.sleep(0.5)
        andar_direita_tras(7)
    if not tem_boss():
        andar_tras(1)
        andar_direita(10)
    if not tem_boss():
        andar_tras(1)
        andar_direita(3.5)
    print("Sair caminho 2")

def vale_desperto(bp, mula):
    time.sleep(1)
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    preparacao()
    pyautogui.moveTo(198, 200)
    time.sleep(2)
    pyautogui.click()
    limpar_entrada()
    dg4()
    while entrada_disponivel(False):
        entrar(False)
        start()
        usar_buff()
        boss1()
        while(not tem_boss()):
            caminho1()
            keyboard.send('z')
            if not tem_boss():
                andar_frente(2)
                andar_direita(3)
        boss2()
        while(not tem_boss()):
            caminho2()
            keyboard.send('z')
            if not tem_boss():
                andar_tras(2)
                andar_direita(1)
        matar_boss_vale_desperto()
        finalizar(bp, mula)
        resgatar_presente()
        preparacao()
        pyautogui.moveTo(198, 200)
        time.sleep(2)
        pyautogui.click()
        dg4()
        time.sleep(1)
    else:
        fechar()





def catacumba_desperta(bp, mula):
    time.sleep(1)
    pyautogui.moveTo(625, 479)
    time.sleep(1)
    pyautogui.rightClick()
    preparacao()
    pyautogui.moveTo(625, 107)
    time.sleep(2)
    pyautogui.click()
    limpar_entrada()
    if tela_dg():
        dg6()
        time.sleep(0.2)
        pyautogui.moveTo(287, 165)
        time.sleep(1.6)
        # Verifica se a imagem alvo está presente na coordenada especificada
        while entrada_disponivel(False):
            # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
            entrar(False)
            start()
            pyautogui.moveTo(402, 132)
            time.sleep(2)
            pyautogui.click()
            pyautogui.moveTo(402, 132)
            time.sleep(2)
            pyautogui.click()
            pyautogui.moveTo(450, 132)
            time.sleep(2)
            pyautogui.click()
            pyautogui.moveTo(450, 132)
            time.sleep(2)
            pyautogui.click()
from comandos import *

def asa_caminho1():
    andar_direita_frente(10)
    pyautogui.moveTo(450, 150)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    quebrar_portao()
    andar_direita_frente(2)
    time.sleep(1)
    andar_esquerda_frente(3)
    matar_monstros()
    time.sleep(5)
    keyboard.send('z')

def chave(bp, mula):
    inicio_pt1()
    andar_esquerda_tras(1)
    inicio_pt2(482, 364)
    if tela_dg():
        dg1()
        while teste_entrar():
            entrar(False)
            asa_caminho1()
            while not tem_boss():
                asa_caminho1()
            matar_boss("bm3")
            andar_esquerda_frente(3)
            andar_tras(2)
            x = 1
            keyboard.send('z')
            while (pyautogui.locateOnScreen(img_bau_reliquia) is None):
                funcao = andar[x%11]
                funcao()
                x+=1
                keyboard.send('z')
            quebrar_bau("bau")
            andar_frente(0.2)
            andar_esquerda(8)
            pyautogui.moveTo(395, 220)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.5)
            andar_direita(0.3)
            keyboard.send('2')
            time.sleep(7)
            andar_esquerda(4)
            while not tem_boss():
                recolher_alz()
                selecionar()
                atacar()
            matar_boss("bm3")  

            andar_frente(2.8)
            quebrar_bau("reliquia")
            andar_frente(4)
            andar_direita_frente(6)
            andar_frente(2)
            andar_esquerda_frente(2)
            pyautogui.moveTo(305,166)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.5)
            andar_tras(0.5)
            time.sleep(0.5)
            quebrar_portao()
            
            andar_esquerda_frente(1.3)
            andar_esquerda(1.4)
            andar_esquerda_tras(5.2)
            procurar_menino()

            keyboard.send('z')
            time.sleep(0.5)
            matar_monstros()
            andar_direita_frente(2)
            keyboard.send('z')
            time.sleep(0.5)
            matar_monstros()
            andar_direita_frente(2)
            keyboard.send('z')
            time.sleep(0.5)
            matar_monstros()
            andar_esquerda_frente(2)
            keyboard.send('z')
            time.sleep(0.5)
            matar_monstros()
            time.sleep(3)
            keyboard.send('z')
            matar_boss("bm3")
            
            andar_esquerda_frente(2)
            andar_tras(1.3)
            quebrar_bau("legado")
            andar_esquerda(10)
            andar_frente(1.8)
            pyautogui.moveTo(215,200)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(0.5)
            andar_direita(0.2)
            quebrar_portao()
            time.sleep(2)
            andar_esquerda(1)
            matar_monstros()
            andar_esquerda_frente(1)
            matar_monstros()
            andar_esquerda_frente(1)
            matar_monstros()
            andar_esquerda_frente(1)
            matar_monstros()
            andar_esquerda_frente(0.8)
            matar_monstros()
            andar_esquerda_frente(1.5)
            for i in range(100):
                print('procurar boss asa')
                if pyautogui.locateOnScreen(boss) is None:
                    keyboard.send('z')
                    time.sleep(0.5)
                else:
                    break
            matar_boss("bm3", usar_hp=True)
            cancelar_bm()
            andar_esquerda_frente(2)
            quebrar_bau("bau")
            time.sleep(5)
            matar_monstros()
            quebrar_bau("bau")
            time.sleep(2)
            andar_esquerda_frente(5)
            time.sleep(4)
            quebrar_bau("legendario")
            time.sleep(10)
            print("finalizar")
            finalizar(bp, mula)
            inicio_pt1()
            andar_esquerda_tras(1)
            inicio_pt2(482, 364)
            if tela_dg():
                dg1()
                time.sleep(1)
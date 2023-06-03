from comandos import *

def selecionar_dificuldade(dificuldade):
    if dificuldade == "facil":
        dg1()
    elif dificuldade == "medio":
        dg2()
    elif dificuldade == "dificil":
        print("caverna do panico Difícil")
        dg3()
    elif dificuldade == "premium":
        dg4()
    elif dificuldade == "elite":
        print("caverna do panico Elite")
        dg5()

def caminho_caverna1():
    tem_monstro_especifico(img_plus, True)
    andar_direita(1.7)
    andar_direita_tras(4)
    andar_tras(1)
    andar_direita_tras(4)
    andar_tras(1)
    andar_direita_tras(4)
    andar_tras(1)
    andar_esquerda(4)

def caminho_caverna2():
    tem_monstro_especifico(img_plus2, True)
    andar_tras(3)
    andar_direita(5)
    andar_tras(1)
    andar_direita_tras(2)
    andar_direita(2)
    andar_direita_tras(3)
    andar_direita(2)
    andar_direita_tras(5)
    andar_tras(3)
    andar_direita_tras(3)
    andar_direita(3)

def caminho_caverna3():
    tem_monstro_especifico(img_plus2, True)
    andar_direita_tras(2)
    andar_tras(2)
    andar_direita_tras(15)
    andar_direita(3)
    andar_direita_tras(3)

def caverna_do_panico(bp=False, mula=False, dificuldade = "dificil"):
    inicio_pt1()
    inicio_pt2(580, 160)
    if tela_dg():
        selecionar_dificuldade(dificuldade)
        while entrada_disponivel(False):
            entrar(False)
            andar_esquerda_tras(2)
            pyautogui.moveTo(200,237)
            time.sleep(0.2)
            pyautogui.click()
            time.sleep(1)
            for i in range(5):
                keyboard.send('space')
                time.sleep(0.5)
            while not get_alvo_encontrado():
                caminho_caverna1()
            matar_monstro_especifico(img_plus)
            set_alvo_encontrado(False)
            while not get_alvo_encontrado():
                caminho_caverna2()
            matar_monstro_especifico(img_plus2)
            set_alvo_encontrado(False)
            while not get_alvo_encontrado():
                caminho_caverna3()
            matar_monstro_especifico(img_plus2)
            set_alvo_encontrado(False)
            # matar_monstro_especifico()
            # while pyautogui.locateOnScreen(elite) is None:
            #     caminho_morada_d1()
            # matar_elite()
            # while pyautogui.locateOnScreen(elite) is None:
            #     caminho_morada_d2()
            # matar_elite()
            # while pyautogui.locateOnScreen(img_portao_morada_d) is None:
            #     caminho_morada_d3()
            # while existem_monstros():
            #     atacar()
            # time.sleep(5)
            # keyboard.send('z')
            # while not tem_boss():
            #     caminho_morada_d4()
            # matar_boss('bm3')
            # quebrar_bau('bau')
            # finalizar(bp, mula)
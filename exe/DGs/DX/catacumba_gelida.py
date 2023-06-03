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
    tem_monstro_especifico(img_plus, True)
    andar_direita(3)
    andar_tras(1)
    andar_direita_tras(8)
    andar_tras(1)
    andar_esquerda(4)

def caminho_caverna3():
    andar_direita_tras(4)
    andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(4)
        andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(9)

def catacumba_gelida(bp=False, mula=False, dificuldade = "dificil"):
    inicio_pt1()
    inicio_pt2(625, 107)
    if tela_dg():
        selecionar_dificuldade(dificuldade)
        while entrada_disponivel(False):
            entrar(False)
            andar_frente(1)
            matar_monstros()
            andar_esquerda(2)
            clique_em(445,380)
            keyboard.send("space")
            keyboard.send("space")
            andar_direita_frente(2)
            andar_esquerda(4)
            andar_esquerda_frente(3)
            andar_frente(2)
            andar_esquerda(3)
            clique_em(312,350)
            keyboard.send("space")
            keyboard.send("space")
            cont = 1
            while cont > 0:
                cont = 0
                for i in range(3):
                    if not tem_monstro_especifico(img_pilha_de_ossos_congelados):
                        atacar()
                        cont += 1
                        keyboard.send('z')
            andar_frente(3)
            andar_tras(2)
            andar_esquerda(6)
            matar_monstros()
            andar_frente(2)
            andar_esquerda(3)
            clique_em(375,392)
            keyboard.send("space")
            andar_direita(7)
            cont = 1
            while cont > 0:
                cont = 0
                for i in range(3):
                    if not tem_monstro_especifico(img_pilha_de_ossos_congelados):
                        atacar()
                        cont += 1
                    keyboard.send('z')

def catacumba_desperta(bp, mula):
    inicio_pt1()
    inicio_pt2(625, 107)
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
            usar_buff()
            andar_frente(1)
            keyboard.send('z')
            matar_boss('bm3')
            andar_frente(3)
            andar_tras(2)
            pyautogui.moveTo(155, 349)
            time.sleep(0.5)
            pyautogui.click()
            keyboard.send('space')
            time.sleep(0.5)
            andar_frente(3)
            andar_esquerda(3)
            andar_esquerda_frente(3)
            andar_frente(2)
            andar_direita(3)
            pyautogui.moveTo(411, 205)
            time.sleep(0.5)
            pyautogui.click()
            time.sleep 
            andar_direita(2)
            matar_monstro_ate_boss()
            matar_boss("bm3")
            quebrar_bau('bau')
            andar_direita(2)
            time.sleep(1)
            pyautogui.moveTo(513, 341)
            time.sleep(1)
            pyautogui.click()
            time.sleep(0.5)
            keyboard.send('space')
            time.sleep(0.5)
            andar_esquerda(13)
            matar_boss("bm2")
            quebrar_bau('bau')
            andar_esquerda(2)
            pyautogui.moveTo(411, 205)
            time.sleep(0.5)
            pyautogui.click()
            # finalizar(bp, mula)
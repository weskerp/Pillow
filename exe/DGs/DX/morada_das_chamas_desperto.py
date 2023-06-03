from comandos import *

def selecionar_dificuldade(dificuldade):
    if dificuldade == "facil":
        dg1()
    elif dificuldade == "medio":
        dg2()
    elif dificuldade == "dificil":
        print("Morada das Chamas Difícil")
        dg3()
    elif dificuldade == "premium":
        dg4()
    elif dificuldade == "elite":
        print("Morada das Chamas Elite")
        dg5()

def caminho_morada_d1():
    # caminho1
    keyboard.send('z')
    if not tem_monstro_especifico(elite):
        print('entrar caminho d1')
        andar_tras(0.3)
        andar_esquerda_frente(4)
        andar_frente(0.5)
        keyboard.send('z')
    if not tem_monstro_especifico(elite):
        andar_esquerda_frente(2)
        andar_frente(0.5)
        keyboard.send('z')
    if not procurar_elite():
        andar_esquerda_frente(2)
        andar_frente(0.5)
        andar_esquerda_frente(4)
        keyboard.send('z')
    if not procurar_elite():
        andar_frente(7)
        time.sleep(0.5)
        keyboard.send('z')
        print('sair caminho d1')

def caminho_morada_d2():
    keyboard.send('z')
    if not tem_monstro_especifico(elite):
        print('entrar caminho d2')
        andar_frente(2)
        andar_tras(0.2)
        keyboard.send('z')
    if not tem_monstro_especifico(elite):
        andar_esquerda_frente(6.5)
        keyboard.send('z')
    if not procurar_elite():
        andar_esquerda_tras(1.5)
        andar_esquerda(3.6)
        keyboard.send('z')
        print('sair caminho d2')

def caminho_morada_d3():
    andar_tras(2)
    andar_esquerda(4)
    andar_esquerda_frente(2)
    andar_esquerda(2)
    andar_esquerda_frente(2)
    andar_esquerda(2)
    andar_esquerda_frente(2)
    andar_esquerda(2)
    andar_esquerda_frente(2)
    andar_frente(1)
    andar_esquerda(1)
    time.sleep(1)
    pyautogui.moveTo(515, 105)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)

def caminho_morada_d4():
    if not tem_boss():
        andar_esquerda_frente(1)
    if not tem_boss():
        andar_frente(5)
    if not tem_boss():
        andar_direita_frente(2)
        keyboard.send('z')

def morada_desperta(bp, mula):
    inicio_pt1()
    inicio_pt2(300,60)
    if tela_dg():
        dg6()
        time.sleep(0.2)
        pyautogui.moveTo(287, 165)
        time.sleep(1.6)
        # Verifica se a imagem alvo está presente na coordenada especificada
        while entrada_disponivel(False):
            # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
            entrar(False)
            andar_esquerda_frente(2)
            keyboard.send('z')
            matar_boss('bm3')
            quebrar_bau('bau')
            while pyautogui.locateOnScreen(elite) is None:
                caminho_morada_d1()
            matar_elite()
            while pyautogui.locateOnScreen(elite) is None:
                caminho_morada_d2()
            matar_elite()
            while pyautogui.locateOnScreen(img_portao_morada_d) is None:
                caminho_morada_d3()
            while existem_monstros():
                atacar()
            time.sleep(5)
            keyboard.send('z')
            while not tem_boss():
                caminho_morada_d4()
            matar_boss('bm3')
            quebrar_bau('bau')
            finalizar(bp, mula)
            inicio_pt1()
            inicio_pt2(300,60)
            if tela_dg():
                dg6()
                time.sleep(0.2)
                pyautogui.moveTo(287, 165)
                time.sleep(1.6)


def caminho_morada1():
    andar_direita(1.7)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(8)
    if not tem_monstro_especifico(img_plus):
        andar_tras(1)
        andar_direita_tras(4)
    if not tem_monstro_especifico(img_plus):
        andar_tras(1)
        andar_esquerda(4)

def caminho_morada2():
    andar_direita(3)
    andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(8)
        andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_esquerda(4)

def caminho_morada3():
    andar_direita_tras(4)
    andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(4)
        andar_tras(1)
    if not tem_monstro_especifico(img_plus):
        andar_direita_tras(9)

def morada_das_chamas(bp=False, mula=False, dificuldade = "dificil"):
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    inicio_pt1()
    inicio_pt2(300,60)
    if tela_dg():
        selecionar_dificuldade(dificuldade)
        while entrada_disponivel(False):
            entrar(False)
            andar_tras(7)
            andar_esquerda_frente(3)
            tem_monstro_especifico(img_urso)
            matar_monstro_especifico(img_urso)
            andar_esquerda_frente(1.5)
            tem_monstro_especifico(img_urso)
            matar_monstro_especifico(img_urso)
            andar_direita_tras(4)
            tem_monstro_especifico(img_golemjr)
            matar_monstro_especifico(img_golemjr)
            andar_esquerda_frente(3)
            andar_frente(3)
            tem_monstro_especifico(img_golemjr)
            matar_monstro_especifico(img_golemjr)
            andar_esquerda(4)
            andar_frente(3)
            tem_monstro_especifico(img_golemjr)
            matar_monstro_especifico(img_golemjr)
            andar_esquerda_frente(6)
            andar_frente(2)
            andar_esquerda(4)
            andar_frente(2)
            andar_esquerda(4)
            tem_monstro_especifico(img_golemjr)
            matar_monstro_especifico(img_golemjr)
            andar_frente(1)
            andar_esquerda_frente(5)
            andar_frente(7)
            matar_monstros()
            andar_esquerda_frente(5)
            time.sleep(10)
            tem_monstro_especifico(img_espirito_da_lava)
            matar_monstro_especifico(img_espirito_da_lava)
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(2)
            andar_frente(3)
            andar_esquerda_frente(2)
            andar_frente(2)
            andar_esquerda_frente(3)
            matar_monstros()
            andar_direita_tras(2)
            andar_tras(2)
            andar_direita_tras(2)
            andar_tras(2)
            andar_esquerda(4)
            andar_esquerda_frente(3)
            tem_boss()
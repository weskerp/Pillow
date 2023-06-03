from comandos import *
def caminhoCastelo1():
    andar_esquerda_frente(3.5)
    andar_frente(1.2)
    andar_esquerda_frente(6)
    andar_esquerda(1.8)
    andar_esquerda_tras(7)
    andar_tras(1)
    andar_direita_tras(15)

def caminhoCastelo2():
    andar_tras(5)
    andar_esquerda_tras(8)
    andar_tras(4)
    andar_esquerda_tras(4)
    andar_esquerda(1)
    andar_tras(1)
    andar_esquerda_tras(9)
    pyautogui.moveTo(130,209)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    quebrar_portao()
    andar_esquerda_tras(8)
    andar_esquerda(5)

def caminhoCastelo3():
    andar_tras(17)
    andar_esquerda(4)
    andar_esquerda_tras(5)
    andar_tras(5)
    andar_esquerda_tras(5)
    andar_esquerda(5)
    andar_esquerda_frente(4)
    andar_esquerda(3)
    andar_frente(2)
    andar_esquerda_frente(2.8)
    andar_direita(3)
    clique_em(322, 213)
    keyboard.send('1')
    andar_tras(3)
    andar_direita_tras(8)
    andar_direita(2)
    andar_direita_tras(3)

def caminhoCastelo4():
    andar_esquerda(4)
    andar_esquerda_frente(4)
    andar_esquerda(3)
    andar_frente(2)
    andar_esquerda(3)
    andar_frente(1)
    andar_esquerda_frente(2)
    andar_esquerda_tras(2)
    andar_esquerda(3)
    andar_frente(1)
    andar_esquerda(3)

def caminhoCastelo5():
    andar_frente(3)
    andar_direita(0.5)
    andar_direita_frente(13)
    andar_frente(4)
    andar_direita(5)
    andar_direita_tras(10)
    andar_direita(3)
    andar_frente(7)
    clique_em(442,210)
    keyboard.send(3)
    keyboard.send('space')
    andar_tras(3)

def caminhoCastelo6():
    andar_direita(3)
    andar_direita_frente(5)
    andar_frente(7)
    andar_esquerda(6)
    andar_esquerda_tras(5)

def caminhoCastelo7():
    andar_esquerda_frente(3)
    andar_frente(2.7)
    andar_direita_frente(3)    
    andar_esquerda_frente(6)
    andar_esquerda(3.5)
    andar_frente(0.5)
    andar_esquerda_frente(4)
    andar_esquerda(2)

def caminhoCastelo8():
    andar_tras(4)
    andar_esquerda_tras(2)
    andar_tras(6)
    andar_esquerda_tras(9)
    andar_direita_tras(6)
    andar_tras(0.5)
    andar_direita(6)
    clique_em(325,390)
    time.sleep(0.5)
    keyboard.send("space")
    andar_esquerda(4)
    andar_tras(2)

def caminhoCastelo9():
    andar_esquerda_tras(5)
    andar_esquerda(12)
    andar_tras(2)
    andar_direita(3)
    andar_direita_tras(4)
    andar_tras(1)

def caminhoCastelo10():
    time.sleep(1)
    andar_tras(7)
    andar_direita_tras(4)
    andar_tras(6)

def caminhoCastelo11():
    andar_esquerda(3)
    andar_esquerda_frente(4)
    andar_esquerda(3)
    andar_esquerda_frente(5)
    andar_frente(1)
    andar_esquerda_frente(3)
    andar_frente(1)
    andar_esquerda_frente(3)
    andar_esquerda_frente(3)
    andar_tras(0.5)
    andar_esquerda_frente(5)
    andar_frente(5)
    andar_frente(2)
    andar_direita_frente(2)
    andar_direita(3)
    andar_direita_tras(1)
    andar_direita(3)
    andar_direita_frente(3)
    andar_frente(5)

def caminhoCastelo12():
    andar_direita_frente(4)
    andar_direita(2)

def caminhoCastelo13():
    andar_direita(6)
    andar_frente(5)
    andar_direita_frente(5)
    andar_direita(2)
    matar_monstros()
    andar_direita_frente(4)
    andar_frente(2)
    andar_direita_frente(4)
    
def caminhoCastelo14():
    andar_esquerda(4)
    andar_frente(3)
    andar_direita_frente(3)
    andar_direita(2)

    
def castelo_das_ilusoes(gema = False, bp = False, mula = False):
    setClasse()
    inicio_pt1()
    andar_tras(1)
    inicio_pt2(205, 240)
    if tela_dg():
        dg1()
        while entrada_disponivel(False):
            time.sleep(0.5)
            entrar(False)
            andar_esquerda_tras(2)
            clique_em(242,330)
            time.sleep(0.5)
            keyboard.send('space')
            time.sleep(0.5)
            keyboard.send('space')
            time.sleep(0.2)
            
            # FAELO
            caminhoCastelo1()
            procurar_boss()
            matar_boss("nobm")
            time.sleep(3)
            quebrar_bau("bau")

            # TARTAMINUS
            caminhoCastelo2()
            procurar_boss()
            matar_boss("bm3")
            andar_esquerda(3)
            quebrar_bau("reliquia")

            # BOSS UP1
            caminhoCastelo3()
            procurar_boss()
            matar_boss2("bm3", False)
            time.sleep(0.2)
            quebrar_bau("bau")

            # BOSS UP2
            caminhoCastelo4()
            procurar_boss()
            matar_boss("bm3")
            quebrar_bau("reliquia")

            # BONE AXE
            caminhoCastelo5()
            while pyautogui.locateOnScreen(img_bau_legado, region=region_c_u) is None:
                caminhoCastelo6()
                procurar_boss()
                matar_boss2("bm3", False)
                tem_monstro_especifico(img_bau_legado)
            cancelar_bm()
            time.sleep(2)
            quebrar_bau("legado")

            # BAU FAKE
            caminhoCastelo7()
            quebrar_bau('legado')
            time.sleep(38)

            # BOSS HARPIA1
            caminhoCastelo8()
            procurar_boss()
            matar_boss("bm3")
            quebrar_bau("bau")

            caminhoCastelo9()
            clique_em(400,400, False)
            quebrar_portao()

            # BOSS HARPIA2
            caminhoCastelo10()
            matar_monstro_ate_boss()
            matar_boss("bm3")
            quebrar_bau("bau")
            
            caminhoCastelo11()
            clique_em(436,177,False)
            quebrar_portao()

            # MAGA
            caminhoCastelo12()
            procurar_boss()
            matar_boss("bm3")
            time.sleep(0.5)
            quebrar_bau("bau")

            # LYCANUS1
            caminhoCastelo13()
            procurar_boss()
            matar_boss2("bm3", False)
            quebrar_bau("bau")

            # LYCANUS2
            caminhoCastelo14()
            procurar_boss()
            matar_boss("bm3")
            quebrar_bau("bau")

            andar_direita_frente(4)
            andar_frente(2)
            clique_em(250,400)
            time.sleep(0.5)
            keyboard.send("space")
            time.sleep(0.5)
            finalizar(bp, mula)
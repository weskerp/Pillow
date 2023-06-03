from comandos import *

def selecionarDificuldade(dificuldade):
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

def locomotivaLouca(bp=False, mula=False, dificuldade = "dificil"):
    inicio_pt1()
    inicio_pt2(575, 110)
    if tela_dg():
        selecionarDificuldade(dificuldade)
        while entrada_disponivel(False):
            entrar(False)
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(2)
            matar_monstros()
            andar_direita_tras(22)
            andar_esquerda_frente(2)
            matar_monstros()
            andar_esquerda_frente(20)
            tem_monstro_especifico(img_portao)
            quebrar_portao()
            andar_esquerda_frente(4)
            procurar_boss()
            matar_boss("bm3")
            time.sleep(0.5)
            quebrar_bau("bau")
            andar_esquerda_frente(6)
            tem_monstro_especifico(img_sleak)
            matar_monstro_especifico(img_sleak)
            andar_esquerda_frente(3)
            clique_em(308,266, False)
            time.sleep(0.5)
            quebrar_portao()
            andar_esquerda_frente(18)
            procurar_boss()
            matar_boss("bm3")
            time.sleep(0.5)
            quebrar_bau("legendario")
            time.sleep(2)
            andar_esquerda_frente(2)
            clique_em(308,266, False)
            time.sleep(0.5)
            keyboard.send("space")
            time.sleep(0.5)
            keyboard.send("space")
            time.sleep(0.5)
            keyboard.send("space")
            time.sleep(0.5)
            keyboard.send("space")
            finalizar(bp, mula)
            
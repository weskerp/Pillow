from comandos import *

def ilhaProibida(gema = False, bp = False, mula = False):
    inicio_pt1()
    andar_direita_tras(3)
    inicio_pt2(660, 360)
    if tela_dg():
        dg1()
        time.sleep(1)
        # Verifica se a imagem alvo está presente na coordenada especificada
        while entrada_disponivel(False):
            # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
            entrar(False)

            andar_esquerda_frente(1.5)
            time.sleep(1)
            pyautogui.moveTo(325,465)
            time.sleep(1)
            pyautogui.click()
            for i in range (9):
                time.sleep(0.2)
                keyboard.send('space')
            andar_esquerda_frente(4)
            andar_frente(3.5)
            time.sleep(0.5)
            keyboard.send('z')
            matar_boss("bm3")
            time.sleep(0.5)
            quebrar_bau('bau')

            andar_frente(3)
            andar_esquerda_tras(14)
            andar_esquerda(4)
            andar_frente(3)
            matar_monstro_especifico(img_gigante)
            andar_frente(5)
            andar_esquerda(4)
            matar_monstro_especifico(img_boto_cruel)
            andar_esquerda_frente(3)
            andar_frente(1.5)
            keyboard.send('z')
            matar_boss("bm3")
            time.sleep(0.5)
            quebrar_bau('bau')

            andar_esquerda(2)
            andar_direita_frente(3)
            andar_esquerda_frente(0.5)
            andar_frente(2.5)
            andar_direita(2.8)
            matar_monstros()
            andar_tras(3.5)
            andar_direita(4)
            andar_direita_tras(5)
            if tem_monstro_especifico(boss):
                matar_boss("bm3")
            quebrar_bau("reliquia")
            andar_frente(5)
            andar_frente(3)
            andar_esquerda_frente(3)
            andar_direita_frente(8)
            andar_frente(3)
            andar_direita(2)
            andar_direita_frente(3)
            andar_direita(3)
            andar_tras(2)

        
      
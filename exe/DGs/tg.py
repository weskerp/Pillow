from comandos import *

def caminhoTg():
    set_pausar_codigo_principal(False)
    usar_buff()
    andar_esquerda_frente(30)
    while not pausar_principal() and getAcabouTempo():
        atacar()
    if pausar_principal():
        caminhoTg()
    
def tg3():
    contarTempo(12000)
    esta_vivo()
    preparacao()
    while pyautogui.locateOnScreen(imgLobyTg):
        time.sleep(15)
    time.sleep(5)
    caminhoTg()
    global cancelar_esta_vivo
    cancelar_esta_vivo = True

    # morreu 374,320
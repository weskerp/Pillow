from comandos import *
from asa import asa_caminho1
from  DGs.ilhaProibida import ilhaProibida
from  DGs.altarSiena1SS import altarSiena1SS
from rodar import rodar
from dxd import *
from DGs.DX.morada_das_chamas_desperto import *
from DGs.DX.catacumbaGelida import *
from DGs.DXD.locomotivaLouca import *
from arena_do_eterno import *
from DGs.castelo_das_ilusoes import *
from up_sn_capella import *
from DGs.tg import *

bp = False
mula = False
def entrar_canal_5():
    time.sleep(1)
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    while(1):
        pyautogui.moveTo(430, 343)
        time.sleep(0.2)
        pyautogui.click()
            
            
            
def teste():
    
    time.sleep(1)
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    
    
    
    matar_boss('nobm')
    andar_direita(5)
    andar_tras(2)
    andar_direita(3)
    matar_monstro_ate_boss()
    matar_boss('nobm')
    andar_direita(2)
    andar_esquerda(0.5)
    andar_tras(6)


    
    
    # entrar_canal_5()
    # for i in range(100):
    #     rodar()
    # catacumba_gelida(dificuldade="premium")

    # while(True):
    #     up_sn()
        
    # matar_monstros()
    # andar_direita_frente(5)
    # andar_direita(5)
    # matar_monstros()
    # andar_direita(3)
    # clique_em()
# teste()
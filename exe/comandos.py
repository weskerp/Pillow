import keyboard
import time
import pyautogui
import threading
from imagens import *

sinergia1 = 'bbab'
sinergia2 = 'bbab'
sinergia3 = 'baab'
# classe = 'DU'
# classe = 'MA'
classe = 'AA'
bm2_active = False
bm3_active = False
aura_active = False
aba = 1
bm3_resfriando = False
bm2_resfriando = False
pausar_codigo_principal = False
cancelar_esta_vivo = False
alvo_encontrado = False
acabouTempo = False


def getAcabouTempo():
    global acabouTempo
    return acabouTempo

def tempoDg(tempo):
    global acabouTempo
    acabouTempo = False
    time.sleep(tempo)
    acabouTempo = True

def switchEnemy():
    global acabouTempo
    
    while not acabouTempo:
        keyboard.send('z')
        time.sleep(0.5)

def contarTempo(tempo):
    t_tempoDg = threading.Thread(target=tempoDg, args=([tempo]))
    t_tempoDg.start()
    t_switchEnemy = threading.Thread(target=switchEnemy)
    t_switchEnemy.start()

# REGIOES DA TELA DO CABAL
left, top, width, height = 0, 0, 800, 600
region = (left, top, width, height)

left_1, top_1, width_1, height_1 = 0, 0, 400, 300
region_1 = (left_1, top_1, width_1, height_1)

left_2, top_2, width_2, height_2 = 300, 0, 800, 300
region_2 = (left_2, top_2, width_2, height_2)

left_3, top_3, width_3, height_3 = 0, 400, 800, 600
region_3 = (left_3, top_3, width_3, height_3)

left_4, top_4, width_4, height_4 = 300, 400, 800, 600
region_4 = (left_4, top_4, width_4, height_4)

left_c, top_c, width_c, height_c = 200, 150, 600, 450
region_c = (left_c, top_c, width_c, height_c)

left_c_u, top_c_u, width_c_u, height_c_u = 150, 0, 550, 300
region_c_u = (left_c_u, top_c_u, width_c_u, height_c_u)

def teste_entrar():
    print('teste entrar')
    if pyautogui.locateOnScreen(img_entrar) is not None  or pyautogui.locateOnScreen(img_entrar2) is not None:
        return True
    else:
        return False
    
# MOVIMENTOS
def andar_direita(tempo = 3):
    print("andar direita")
    time.sleep(0.2)
    keyboard.press('e')
    time.sleep(tempo)
    keyboard.send('e')

def andar_esquerda(tempo = 3):
    print("andar esquerda")
    time.sleep(0.2)
    keyboard.press('q')
    time.sleep(tempo)
    keyboard.send('q')

def andar_frente(tempo = 3):
    print("andar frente")
    time.sleep(0.2)
    keyboard.press('w')
    time.sleep(tempo)
    keyboard.send('w')

def andar_tras(tempo = 3):
    print("andar traz")
    time.sleep(0.2)
    keyboard.press('s')
    time.sleep(tempo)
    keyboard.send('s')

def andar_direita_frente(tempo = 3):
    print("andar direita frente")
    time.sleep(0.2)
    keyboard.press('e')
    keyboard.press('w')
    time.sleep(tempo)
    keyboard.send('e')
    keyboard.send('w')

def andar_direita_tras(tempo = 3):
    print("andar direita traz")
    time.sleep(0.2)
    keyboard.press('e')
    keyboard.press('s')
    time.sleep(tempo)
    keyboard.send('e')
    keyboard.send('s')

def andar_esquerda_frente(tempo = 3):
    print("andar esquerda frente")
    time.sleep(0.2)
    keyboard.press('q')
    keyboard.press('w')
    time.sleep(tempo)
    keyboard.send('q')
    keyboard.send('w')

def andar_esquerda_tras(tempo = 3):
    print("andar esquerda traz")
    time.sleep(0.2)
    keyboard.press('q')
    keyboard.press('s')
    time.sleep(tempo)
    keyboard.send('q')
    keyboard.send('s')

andar= [ andar_esquerda,andar_frente,andar_direita,andar_tras, andar_esquerda_frente, andar_direita, andar_esquerda_tras, andar_frente, andar_direita_tras, andar_esquerda, andar_direita_frente]
 
def resgatar_presente():
    time.sleep(1)
    pyautogui.moveTo(165, 610)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(535, 485)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(709, 519)
    time.sleep(1)
    pyautogui.click()
    time.sleep(1)
    
# MOUSE
def entrada_disponivel(gemas):
    if gemas:
        if pyautogui.locateOnScreen(entrar_gemas_2_img) is not None:
            return True
        else:
            return False
    else:
        if pyautogui.locateOnScreen(img_entrar) is not None  or pyautogui.locateOnScreen(img_entrar2) is not None:
            return True
        else:
            return False
        
def entrar(gemas):
    print("entrar")
    time.sleep(1)
    if gemas:
        pyautogui.moveTo(571, 543)
    else:
        pyautogui.moveTo(486, 543)
    time.sleep(0.8)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(317, 469)
    time.sleep(1)
    pyautogui.click()
    usar_buff()

def fechar():
    time.sleep(1)
    pyautogui.moveTo(595, 492)
    pyautogui.click()
    
def start():
    time.sleep(2)
    pyautogui.moveTo(317, 469)
    time.sleep(1)
    pyautogui.click()

#SELECIONA A POSIÇÃO DA DG NA TELA DE ESCOLHA 
def dg1():
    time.sleep(1)
    pyautogui.moveTo(165, 180)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg2():
    time.sleep(1)
    pyautogui.moveTo(165, 195)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg3():
    time.sleep(1)
    pyautogui.moveTo(165, 210)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg4():
    time.sleep(1)
    pyautogui.moveTo(165, 225)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg5():
    time.sleep(1)
    pyautogui.moveTo(165, 240)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg6():
    time.sleep(1)
    pyautogui.moveTo(165, 255)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def dg7():
    time.sleep(1)
    pyautogui.moveTo(165, 270)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(287, 155)
    time.sleep(1)

def preparacao():
    print("preparação")
    time.sleep(0.5)
    pyautogui.moveTo(280, 554)
    time.sleep(0.5)
    pyautogui.click()
    keyboard.send("f1")
    global aba
    aba = 1

# DGS
def inicio_pt1():
    time.sleep(1)
    pyautogui.moveTo(669, 479)
    time.sleep(1)
    pyautogui.rightClick()
    preparacao()

def inicio_pt2(x, y):
    time.sleep(0.5)
    pyautogui.moveTo(x, y)
    time.sleep(2)
    pyautogui.click()
    limpar_entrada()
    pyautogui.moveTo(287, 155)

def quebrar_portao_arena():
    time.sleep(1)
    pyautogui.moveTo(341,330)
    time.sleep(0.8)
    pyautogui.click()
    time.sleep(0.8)
    keyboard.send('2')
    time.sleep(6)

def quebrar_portao_arena_esperar():
    quebrar_portao_arena()
    time.sleep(350)

def selecionar():
    time.sleep(0.5)
    keyboard.send('z')

def atacar():
    print("atacar")
    time.sleep(0.2)
    keyboard.send('1')
    time.sleep(0.2)
    keyboard.send('2')
    time.sleep(0.2)
    keyboard.send('3')
    time.sleep(0.2)
    if classe == "AA":
        keyboard.send('-')
        time.sleep(1)
    keyboard.press_and_release('alt + 1')
    keyboard.send('space')
    
def recolher_alz():
    keyboard.send('space')

def quebrar_portao():
    while pyautogui.locateOnScreen(img_portao) is not None:
        atacar()
    time.sleep(4)
        

def quebrar_bau(bau):
    print('quebrar_bau')
    cont = 0
    if(bau == "reliquia"):
        print("reliquia")
        while pyautogui.locateOnScreen(img_bau_reliquia, region=region_c_u) is None:
            time.sleep(0.5)
            keyboard.send('z')
    elif(bau == "legendario"):
        while cont < 100 and pyautogui.locateOnScreen(img_bau_legendario, region=region_c_u) is None:
            print("quebra bau lendario: " + str(cont))
            # time.sleep(0.2)
            keyboard.send('z')
            keyboard.send('space')
            cont = cont + 1
    elif(bau == "legado"):
        print("legado")
        while pyautogui.locateOnScreen(img_bau_legado, region=region_c_u) is None:
            keyboard.send('space')
            keyboard.send('z')
    elif(bau == "bau"):
        print("bau")
        if pyautogui.locateOnScreen(img_bau, region=region_c_u) is None:
            keyboard.send('z')
    time.sleep(0.5)
    keyboard.send('0')
    time.sleep(0.5)
    keyboard.send('0')
    time.sleep(4)
    for i in range(20):
        keyboard.send('space')
        time.sleep(0.2)
  
def perdeu_hp():
    if pyautogui.locateOnScreen(img_perdeu_hp):
        return True
    else:
        return False

def finalizar(bp, mula):
    for i in range(20):
        recolher_alz()
        time.sleep(0.2)
    pyautogui.moveTo(415, 210)
    time.sleep(0.8)
    pyautogui.click()
    if mula:
        time.sleep(0.8)
        pyautogui.moveTo(388, 445)
        time.sleep(0.8)
        pyautogui.click()
        time.sleep(0.8)
        pyautogui.moveTo(346, 445)
        time.sleep(0.8)
        pyautogui.click()
    else:
        if(bp):
            time.sleep(0.8)
            pyautogui.moveTo(611, 445)
            time.sleep(0.8)
            pyautogui.click()
        time.sleep(0.8)
        pyautogui.moveTo(325, 445)
        time.sleep(0.8)
        pyautogui.click()
        time.sleep(0.8)
        pyautogui.moveTo(282, 445)
        time.sleep(0.8)
        pyautogui.click()
        time.sleep(0.8)
    time.sleep(5)
    
def usar_buff():
    print("buff")
    time.sleep(1)
    keyboard.press_and_release("ctrl + 7")
    time.sleep(1.4)

def clique_em(x, y, npc = True):
    pyautogui.moveTo(x, y)
    time.sleep(0.5)
    pyautogui.click()
    time.sleep(0.5)
    for i in range(50):
        if npc and pyautogui.locateOnScreen(img_tela_npc, region=region_1) is None:
            if not existem_monstros():
                pyautogui.moveTo(x, y+i)
            atacar()
            pyautogui.click()
            time.sleep(0.5)

def usar_over_atk():
    print("overbuff atk")
    time.sleep(1)
    keyboard.send("5")
    time.sleep(0.2)
    keyboard.send("6")
    time.sleep(0.2)
    keyboard.send("7")
    time.sleep(0.2)

def usar_over_def():
    print("overbuff def")
    time.sleep(1)
    keyboard.send("8")
    time.sleep(0.2)
    keyboard.send("9")
    time.sleep(0.2)

def ativar_bm3(no_aura = True, switch = False):
    global bm3_active
    if not bm3_active and not bm3_resfriando:
        if no_aura:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([True]))
            t_bm_is_active.start()
        else:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([False]))
            t_bm_is_active.start()
        print("ativar bm3")
        bm3_active = True
        if(classe == 'MA'):
            usar_sp()
        keyboard.send('f2')
        global aba
        aba = 2
        keyboard.press_and_release("alt + 9")
        time.sleep(1)
        keyboard.press_and_release("alt + 9")
        time.sleep(3.1)
        keyboard.press_and_release("alt + 9")
        time.sleep(2.2)
    elif switch and not bm2_active and not bm2_resfriando: 
        if no_aura:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([True]))
            t_bm_is_active.start()
        else:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([False]))
            t_bm_is_active.start()
        print("ativar bm2")
        bm3_active = True
        if(classe == 'MA'):
            usar_sp()
        keyboard.send('f1')
        aba = 2
        keyboard.press_and_release("alt + -")
        time.sleep(1)
        keyboard.press_and_release("alt + -")
        time.sleep(3.1)
        keyboard.press_and_release("alt + -")
        time.sleep(2.2)

def ativar_bm2(no_aura = True):
    global bm2_active
    if not bm2_active and not bm2_resfriando(): 
        if no_aura:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([True]))
            t_bm_is_active.start()
        else:
            t_bm_is_active = threading.Thread(target=bm_is_active, args=([False]))
            t_bm_is_active.start()
        print("ativar bm2")
        bm2_active = True
        if(classe == 'MA'):
            usar_sp()
        time.sleep(2.5)
        keyboard.send('f1')
        global aba
        aba = 1
        time.sleep(0.5)
        keyboard.press_and_release("alt + 8")
        time.sleep(1)
        keyboard.press_and_release("alt + 8")
        time.sleep(2)
        keyboard.press_and_release("alt + 8")
        time.sleep(7)

def ativar_aura():
    print("ativar aura")
    global aura_active
    aura_active = True
    time.sleep(0.5)
    keyboard.press_and_release('alt + 0')
    time.sleep(1.2)

def fatal(trocar_alvo):
    print("fatal")
    if trocar_alvo:
        keyboard.send('z')
    keyboard.send('3')
    time.sleep(2.1)
    keyboard.send("space")

def usar_sp():
    time.sleep(0.5)
    keyboard.press_and_release('alt + 8')
    time.sleep(1.5)

def sp_full():
    if pyautogui.locateOnScreen(img_sp_full) is not None:
        return True
    else:
        return False
    
def sp_2():
    if pyautogui.locateOnScreen(sp) is not None:
        return True
    else:
        return False
    
def sp_1():
    if pyautogui.locateOnScreen(sp_final) is not None:
        return True
    else:
        return False
    
def atacar_bm2():
    print("atacar bm2")
    keyboard.send('0')
    time.sleep(2)
    keyboard.send('space')

def atacar_bm3(sinergia, trocar_alvo):
    print("atacar bm3")
    if(trocar_alvo):
        if sinergia == 'bbab':
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)

        elif sinergia == 'aaba':
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)

        elif sinergia == 'baab':
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('z')
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)

    else:
        if sinergia == 'bbab' :
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)

        elif sinergia == 'aaba':
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)

        elif sinergia == 'baab':
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('1')
            time.sleep(1.3)
            keyboard.send('space')
            keyboard.send('2')
            time.sleep(1.3)

def cancelar_bm():
    print("cancelar bm")
    global bm3_active
    global bm2_active
    global aura_active
    if bm3_active:
        bm3_active = False
        t_bm3_esta_resfriando = threading.Thread(target=bm3_esta_resfriando)
        if not t_bm3_esta_resfriando.is_alive():
            t_bm3_esta_resfriando.start()
    elif bm2_active:
        bm2_active = False
        t_bm2_esta_resfriando = threading.Thread(target=bm2_esta_resfriando)
        if not t_bm2_esta_resfriando.is_alive():
            t_bm2_esta_resfriando.start()
    aura_active = False
    time.sleep(0.5)
    pyautogui.moveTo(139, 103)
    time.sleep(0.6)
    pyautogui.rightClick()
    keyboard.send('f1')
    global aba
    aba = 1
    time.sleep(5)

def desiste_dg():
    cancelar_bm()
    time.sleep(0.5)
    pyautogui.moveTo(756, 121)
    time.sleep(1)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.moveTo(399, 379)
    time.sleep(1)
    pyautogui.click()

def bm_is_active(no_aura = True):
    print("bm esta ativa?")
    time.sleep(90)
    if not no_aura and (bm3_active or bm2_active):
        print("bm esta ativa, ativar aura")
        ativar_aura()
        ativar_aura()
        ativar_aura()
        time.sleep(50)
        global aba
        if aba == 2:
            print("bm esta ativa, aura esta ativa, cancelar bm + aura")
            cancelar_bm()
    elif bm3_active or bm2_active:
        cancelar_bm()

def existem_monstros():
    if pyautogui.locateOnScreen(monstros, region=region_c_u) is not None:
        return True
    else:
        return False
            
def procurar_menino():
    for i in range(20):
        if pyautogui.locateOnScreen(menino_img) is None:
            time.sleep(0.2)
            keyboard.send('z')
    time.sleep(0.5)
    while existem_monstros():
        atacar()
    
def matar_monstros():
    keyboard.send('z')
    while existem_monstros():
        atacar()
        time.sleep(0.2)
        keyboard.send('z')

def tem_boss():
    if pyautogui.locateOnScreen(boss, region=region_c_u) is not None:
        return True
    else:
        return False

def tela_dg():
    print("tela dg")
    if pyautogui.locateOnScreen(img_tela_dg) is not None or pyautogui.locateOnScreen(img_tela_dg2) is not None:
        return True
    else:
        return False
    
def matar_monstro_ate_boss():
    while not tem_boss():
        recolher_alz()
        selecionar()
        atacar()

def procurar_elite():
    for i in range (10):
        if pyautogui.locateOnScreen(elite, region=region_c_u) is None:
            keyboard.send('z')
            time.sleep(0.2)
    if pyautogui.locateOnScreen(elite, region=region_c_u) is not None:
        return True
    else:
        return False

def matar_elite():
    while pyautogui.locateOnScreen(elite) is not None:
        recolher_alz()
        atacar()

def matar_boss(bm, no_aura = False):
    if(bm == 'bm3'):
        if sp_2:   
            ativar_bm3(no_aura)
            while tem_boss():
                atacar_bm3(sinergia1, False)
                if tem_boss():
                    atacar_bm3(sinergia2, False)
                if tem_boss():
                    atacar_bm3(sinergia3, False)
                if tem_boss():
                    fatal(False)
                if classe == "GL" and tem_boss():
                    fatal(False)
                if classe == "GL" and tem_boss():
                    fatal(False)
            cancelar_bm()
        else:
            while tem_boss():
                atacar()
                keyboard.send('space')
    else:
        while tem_boss():
                atacar()
                keyboard.send('space')
def acabou_bm():
    if pyautogui.locateOnScreen(img_bm3_ma) is None:
        return True
    else:
        return False
    
def matar_boss2(bm, no_aura = True):
    print("Matar boss 2")
    if(bm == 'bm3'):
        if sp_2:
            ativar_bm3(no_aura)
            while tem_boss():
                atacar_bm3(sinergia1, False)
                if tem_boss():
                    atacar_bm3(sinergia2, False)
                if tem_boss():
                    atacar_bm3(sinergia3, False)
                if tem_boss():
                    fatal(False)
        else:
            while tem_boss():
                atacar()
                keyboard.send('space')
    else:
        while tem_boss():
                atacar()
                keyboard.send('space')

def dg_falhou():
    if pyautogui.locateOnScreen(img_dg_falhou):
        return True
    else:
        return False
    
def fechar_dg_perdida():
    pyautogui.moveTo()
    time.sleep(1.5)
    pyautogui.click(390, 470)

def limpar_entrada():
    while existem_monstros() and not tela_dg():
        atacar()
        time.sleep(7)
        pyautogui.click()

def set_alvo_encontrado(opcao):
    global alvo_encontrado        
    alvo_encontrado = opcao

def get_alvo_encontrado():
    global alvo_encontrado
    return alvo_encontrado

def search_target(imagem):
    while  pyautogui.locateOnScreen(imagem, region=region_c_u) is None:
        time.sleep(0.5)
        keyboard.send('z')
    set_alvo_encontrado(True)

def tem_monstro_especifico(imagem, andar = False):
    if andar:
        t_search_target = threading.Thread(target=search_target, args=([imagem]))
        t_search_target.start()
    else:
        for i in range(20):
            if pyautogui.locateOnScreen(imagem, region=region_c_u) is not None:
                return True
            else:
                keyboard.send('z')
                time.sleep(0.2)
        return False

def matar_monstro_especifico(imagem):
    while pyautogui.locateOnScreen(imagem, region=region_c_u) is None:
        time.sleep(0.2)
        keyboard.send('z')
    while existem_monstros():
        time.sleep(0.2)
        atacar()

def morreu():
    if pyautogui.locateOnScreen(img_morreu) is not None or pyautogui.locateOnScreen(img_morreu2) is not None:
        return True
    else:
        return False
    
def esta_morto():
    if morreu():
        print("morreu")
        time.sleep(0.5)
        pyautogui.moveTo(400, 425)
        time.sleep(0.2)
        pyautogui.click()
        return True
    else:
        return False
    
def bm2_esta_resfriando():
    global bm2_resfriando
    bm2_resfriando = True
    time.sleep(30)

def bm3_esta_resfriando():
    global bm3_resfriando
    bm3_resfriando = True
    time.sleep(30)
    bm3_resfriando = False
        
def is_alive():
    while not cancelar_esta_vivo:
        if esta_morto():
            global pausar_codigo_principal
            pausar_codigo_principal = True
            print("morreu1: " + str(pausar_codigo_principal))
            time.sleep(5)
            print("morreu2: " + str(pausar_codigo_principal))
            
def esta_vivo():
    t_is_alive = threading.Thread(target=is_alive)
    t_is_alive.start()

def procurar_boss():
    while not tem_boss():
        keyboard.send('z')

def pausar_principal():
    if pausar_codigo_principal:
        return True
    else:
        return False
    
def set_pausar_codigo_principal(op):
    global pausar_codigo_principal
    pausar_codigo_principal = op

def quebrarItens():
    time.sleep(0.5)
    keyboard.send('i')
    clique_em(496,130,False)
    time.sleep(0.5)
    clique_em(505,490,False)
    time.sleep(1)
    clique_em(546,460,False)
    time.sleep(0.5)
    # linha1
    clique_em(505,166,False)
    clique_em(540,166,False)
    clique_em(580,166,False)
    clique_em(620,166,False)
    clique_em(650,166,False)
    clique_em(690,166,False)
    clique_em(730,166,False)
    clique_em(760,166,False)
    # linha2
    clique_em(580,205,False)
    clique_em(620,205,False)
    clique_em(650,205,False)
    clique_em(690,205,False)
    clique_em(730,205,False)
    clique_em(760,205,False)
    # linha3
    clique_em(580,240,False)
    clique_em(620,240,False)
    clique_em(650,240,False)
    clique_em(690,240,False)
    clique_em(730,240,False)
    clique_em(760,240,False)
    # linha4
    clique_em(580,280,False)
    clique_em(620,280,False)
    clique_em(650,280,False)
    clique_em(690,280,False)
    clique_em(730,280,False)
    clique_em(760,280,False)
    # linha5
    clique_em(580,315,False)
    clique_em(620,315,False)
    clique_em(650,315,False)
    clique_em(690,315,False)
    clique_em(730,315,False)
    clique_em(760,315,False)
    # linha6
    clique_em(580,350,False)
    clique_em(620,350,False)
    clique_em(650,350,False)
    clique_em(690,350,False)
    clique_em(730,350,False)
    clique_em(760,350,False)
    # linha7
    clique_em(580,390,False)
    clique_em(620,390,False)
    clique_em(650,390,False)
    clique_em(690,390,False)
    clique_em(730,390,False)
    clique_em(760,390,False)
    # linha8
    clique_em(580,420,False)
    clique_em(620,420,False)
    clique_em(650,420,False)
    clique_em(690,420,False)
    clique_em(730,420,False)
    clique_em(760,420,False)

    clique_em(457,457,False)
    clique_em(422,422,False)
    time.sleep(60)
    clique_em(545,500,False)
    keyboard.send("i")

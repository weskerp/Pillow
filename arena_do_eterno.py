from comandos import *

# ONDAS
def onda(numero):
    if numero == '0':
        print("entrar onda 0")
        if(classe == 'MA'):
            usar_sp()
            while pyautogui.locateOnScreen(img_espera) is None or pausar_principal():
                atacar()
                keyboard.send('z')
                if(pausar_principal()):
                    caminho_arena_eterno()
        print("sair onda 0")

    if numero == '1':
        print("entrar onda 1")
        if(classe == 'MA'):
            usar_sp()
        if sp_2():
            ativar_bm3(switch = True)
            keyboard.send('z')
            while pyautogui.locateOnScreen(img_espera) is None or pausar_principal():
                atacar_bm3('bbab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    atacar_bm3('bbab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    atacar_bm3('baab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    fatal(True)
                if(pausar_principal()):
                    caminho_arena_eterno()
        else:
            while pyautogui.locateOnScreen(img_espera) is None or pausar_principal():
                atacar()
                keyboard.send('z')
                if(pausar_principal()):
                    caminho_arena_eterno()
        print("sair onda 1")

    elif numero == '2':
        print("entrar onda 2")
        if(classe == 'MA'):
            usar_sp()
        if sp_2():
            ativar_bm3(switch = True)
            keyboard.send('z')
            while pyautogui.locateOnScreen(img_espera) is None:
                atacar_bm3('bbab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    atacar_bm3('bbab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    atacar_bm3('baab', True)
                if pyautogui.locateOnScreen(img_espera) is None:
                    fatal(True)
            cancelar_bm()
        else:
            while pyautogui.locateOnScreen(img_espera) is None:
                atacar()
                keyboard.send('z')
        print("sair onda 2")

# ONDAS BOSS
    elif numero == 'boss1':
        print("Entrar boss 1")
        keyboard.send('z')
        if(classe == 'MA'):
            usar_sp()
        usar_over_atk()
        keyboard.send('z')
        matar_boss2('bm3')
        time.sleep(4)
        keyboard.send('z')
        quebrar_bau('bau')
        print("Sair boss 1")  

    elif numero == 'boss2':
        print("Entrar boss 2")
        keyboard.send('z')
        if(classe == 'MA'):
            usar_sp()
        if sp_2():
            ativar_bm3(False, True)
            while tem_boss():
                atacar_bm3(sinergia1, False)
                if tem_boss():
                    atacar_bm3(sinergia2, False)
                if tem_boss():
                    atacar_bm3(sinergia3, False)
                if tem_boss():
                    fatal(False)
            time.sleep(7)
            usar_over_atk()
            keyboard.send('z')
            while tem_boss():
                atacar_bm3(sinergia1, False)
                if tem_boss():
                    atacar_bm3(sinergia2, False)
                if tem_boss():
                    atacar_bm3(sinergia3, False)
                if tem_boss():
                    fatal(False)
            cancelar_bm()
        else:
            matar_boss(False)
            time.sleep(5)
            matar_boss(False)
        quebrar_bau('bau')
        print("Sair boss 2")

def espera():
    while pyautogui.locateOnScreen(img_espera) is not None:
        time.sleep(2)
        
def caminho_arena_eterno():
    usar_buff()
    andar_esquerda_frente(7)
    andar_esquerda_tras(14)
    quebrar_portao_arena()
    andar_esquerda_tras(12)
    
def arena_eterno(gemas, bp, mula):
    print("inicio da arena do eterno")
    cont = 0
    inicio_pt1()
    while(cont==0):
        transform = False
        if not sp_full():
            keyboard.send('f4')
            aba = 4
            time.sleep(0.5)
            keyboard.press_and_release('alt + =')
            transform = True
        while not sp_full():
            if classe == 'MA':
                keyboard.press_and_release('alt + =')
                time.sleep(0.5)
                usar_sp()
                time.sleep(0.5)
                keyboard.press_and_release('alt + =')
            time.sleep(30)
        if transform:
            keyboard.press_and_release('alt + =')
            time.sleep(0.5)
        time.sleep(1)
        preparacao()
        andar_direita(0.8)
        inicio_pt2(290, 179)
        if tela_dg():
            dg1()
            if entrada_disponivel(gemas):
                entrar(gemas)
                esta_vivo()
                caminho_arena_eterno()
                onda('1')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('0')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('boss1')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('boss2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                onda('2')
                # espera()
                if(dg_falhou()):
                    fechar_dg_perdida()
                    continue
                desiste_dg()
                # onda('boss3')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('boss4')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('2')
                # espera()
                # if(dg_falhou()):
                #     fechar_dg_perdida()
                #     continue
                # onda('boss5')
                # finalizar(bp, mula)
                global cancelar_esta_vivo
                cancelar_esta_vivo = True
                dg1()
                time.sleep(0.2)
                pyautogui.moveTo(287, 165)
                time.sleep(1.6)
            else:
                cont = 1
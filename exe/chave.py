from comandos import *


def caminho_arena(esperar):
    preparacao()
    if pyautogui.locateOnScreen(img_asa_verde, region=region_1) is not None:
        andar_esquerda_frente(7.2)
    else:
        andar_esquerda_frente(8)
        
    andar_esquerda_tras(14)
    if(esperar):
        quebrar_portao_arena_esperar()
    quebrar_portao_arena()
    andar_esquerda_tras(12)
    set_pausar_codigo_principal(False)

def matar_boss_arena(bm):
    if bm:
        if classe == 'DU':
            time.sleep(2)
            ativar_bm2()
            cont = 0
            cont2 = 0
            while tem_boss():
                if(cont<60):
                    atacar_bm2()
                    if cont == 40:
                        ativar_aura()
                    cont = cont + 1
                else:
                    if cont2 == 0:
                        cancelar_bm()
                        cont2 = 1
                    else:
                        atacar()
        else:
            time.sleep(2)
            ativar_bm3(False)
            while tem_boss():
                atacar_bm3('bbab', False)
                if tem_boss():
                    atacar_bm3('bbab', False)
                if tem_boss():
                    atacar_bm3('bbab', False)
                if tem_boss():
                    fatal(False)
        cancelar_bm()
    else:
        while tem_boss():   
            atacar() 
    time.sleep(3)   

def procura_boss():
    cont = 0
    x = 0
    while cont == 0:
        print("procurar boss")
        recolher_alz()
        if(pausar_principal()):
            caminho_arena(False)
        for i in range(10):
          if cont == 0 and not tem_boss():
              time.sleep(0.2)
              keyboard.send('z')
              if(not existem_monstros):
                  funcao = andar(x%11)
                  funcao()
                  x+=1
        if cont == 0 and not tem_boss():
            keyboard.send('z')
            time.sleep(0.2)
            atacar()
        else:
            cont = 1
            

def chave(arena, gemas, bp, esperar, mula, bm):
    entrou = 1
    inicio_pt1()
    andar_direita(1.2)
    inicio_pt2(604, 200)
    if tela_dg():
        arena()
        while entrada_disponivel(gemas):
            entrou = 0
            entrar(gemas)
            esta_vivo()
            caminho_arena(esperar)
            if perdeu_hp():
                keyboard.send('8')
            procura_boss()
            usar_over_def()
            matar_boss_arena(bm)        
            while pausar_principal():
                caminho_arena(False)
                procura_boss()
                usar_over_def()
                matar_boss_arena(bm)
            quebrar_bau('legendario')
            finalizar(bp, mula)
            global cancelar_esta_vivo
            cancelar_esta_vivo = True
            resgatar_presente()
            andar_direita(1.2)
            time.sleep(1)
            pyautogui.moveTo(604, 200)
            time.sleep(1)
            pyautogui.click()
            if tela_dg():
                arena()
                pyautogui.moveTo(287, 165)
                time.sleep(1)
    
        fechar()
    return entrou    

def rush(bp, esperar, mula, bm):
    cont = 0
    while cont < 7:
        cont = 0
        cont = cont + chave(dg1, False, bp, esperar, mula, bm)
        cont = cont + chave(dg2, False, bp, esperar, mula, bm)
        cont = cont + chave(dg3, False, bp, esperar, mula, bm)
        cont = cont + chave(dg4, False, bp, esperar, mula, bm)
        cont = cont + chave(dg5, False, bp, esperar, mula, bm)
        cont = cont + chave(dg6, False, bp, esperar, mula, bm)
        cont = cont + chave(dg7, False, bp, esperar, mula, bm)
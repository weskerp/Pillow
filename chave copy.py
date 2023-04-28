import pyautogui
import time
from PIL import Image


def entrar():
    time.sleep(1)
    pyautogui.moveTo(436, 494)
    pyautogui.click()

def fechar():
    time.sleep(1)
    pyautogui.moveTo(595, 492)
    pyautogui.click()

def chave1():
    time.sleep(1)
    pyautogui.moveTo(170, 179)
    pyautogui.click()

def chave2():
    time.sleep(1)
    pyautogui.moveTo(170, 196)
    pyautogui.click()

def chave3():
    time.sleep(1)
    pyautogui.moveTo(170, 208)
    pyautogui.click()

def chave4():
    time.sleep(1)
    pyautogui.moveTo(170, 224)
    pyautogui.click()

def chave5():
    time.sleep(1)
    pyautogui.moveTo(170, 241)
    pyautogui.click()

def chave6():
    time.sleep(1)
    pyautogui.moveTo(170, 256)
    pyautogui.click()

def chave7():
    time.sleep(1)
    pyautogui.moveTo(170, 269)
    pyautogui.click()

def chave(arena, gemas, bp, revive):
    # Define as coordenadas dos pontos que o macro irá clicar
    verificar_coord = (378, 465)

    # Carrega a imagem que o macro deve procurar na tela
    imagem_alvo = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\800x600\\Entrar.png")

    time.sleep(1)
    # Clica no primeiro ponto
    pyautogui.moveTo(669, 479)
    pyautogui.rightClick()
    pyautogui.click()
    # Espera um segundo para a tela atualizar
    time.sleep(1)
    pyautogui.moveTo(760, 323)
    pyautogui.click()

    arena()

    
    time.sleep(2)
    pyautogui.moveTo(verificar_coord)


    # Verifica se a imagem alvo está presente na coordenada especificada
    if pyautogui.locateOnScreen(imagem_alvo) is not None:
        # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
        entrar()
        # pyautogui.keyDown('w')
        # pyautogui.keyDown('a')
        # time.sleep(10)
        # pyautogui.keyUp('w')
        # pyautogui.keyUp('a')
    else:
        # Se a imagem não estiver presente, clica no segundo ponto e encerra
        fechar()

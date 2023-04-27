import pyautogui
import time
from PIL import Image

def chave2():
    # Define as coordenadas dos pontos que o macro irá clicar
    clicar_coord = (311, 41)
    verificar_coord = (385, 484)
    clicar_outro_coord = (300, 300)

    # Carrega a imagem que o macro deve procurar na tela
    imagem_alvo = Image.open("C:\\Users\\iagow\\OneDrive\\Documentos\\800x600\\Entrar.png")

    time.sleep(1)
    # Clica no primeiro ponto
    pyautogui.click(669, 479)
    # Espera um segundo para a tela atualizar
    time.sleep(4)
    pyautogui.click(760, 323)
    time.sleep(2)
    pyautogui.click(760, 323)

    time.sleep(2)


    # Verifica se a imagem alvo está presente na coordenada especificada
    if pyautogui.locateOnScreen(imagem_alvo, region=verificar_coord) is not None:
        # Se a imagem estiver presente, clica no terceiro ponto e segura as teclas 'w' e 'a' por 10 segundos
        pyautogui.click(300, 300)
        pyautogui.keyDown('w')
        pyautogui.keyDown('a')
        time.sleep(10)
        pyautogui.keyUp('w')
        pyautogui.keyUp('a')
    else:
        # Se a imagem não estiver presente, clica no segundo ponto e encerra
        pyautogui.click(verificar_coord)
        pyautogui.click(clicar_outro_coord)

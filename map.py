import win32api

def mapear():
    # Obter as coordenadas atuais do mouse
    x, y = win32api.GetCursorPos()

    # Imprime as coordenadas na tela
    texto = f"x = {x} y = {y}"
    return texto

import win32api
import time


def mapa():
  time.sleep(4)
  # Obter as coordenadas atuais do mouse
  x, y = win32api.GetCursorPos()

  # Imprime as coordenadas na tela
  print("Coordenadas atuais do mouse: x = {}, y = {}".format(x, y))

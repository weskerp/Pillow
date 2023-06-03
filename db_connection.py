import requests

def connection():
    link = "https://macro-weskeys-default-rtdb.firebaseio.com/usuarios/tonyJunior"
    requisicao = requests.get(f'{link}.json')
    dic_requisicao = requisicao.json()
    if dic_requisicao == {'status': 1} :
        return True 
    else:
        return False
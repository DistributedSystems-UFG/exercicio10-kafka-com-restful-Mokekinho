import time
import requests
from const import *


URL_SERVIDOR = "http://" + REST_IP + ":" + REST_PORT + "/temperatura"

print(f"Conectando em: {URL_SERVIDOR}")

def consultar_temperatura():
    print("[-] Iniciando monitoramento de temperatura... (Pressione Ctrl+C para sair)\n")
    
    while True:
        try:
            resposta = requests.get(URL_SERVIDOR)
            

            if resposta.status_code == 200:
                temperatura = resposta.json()

                print(f"[Atualização] {temperatura}")
            else:
                print(f"[!] Erro no servidor: Código {resposta.status_code}")
                
        except requests.exceptions.ConnectionError:
            print("[!] Não foi possível conectar ao servidor Flask. Ele está rodando?")
            
        time.sleep(5)

if __name__ == "__main__":
    consultar_temperatura()
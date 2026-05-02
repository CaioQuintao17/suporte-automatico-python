import socket
import platform
import subprocess

def coletar_rede():
    ip = socket.gethostbyname(socket.getfqdn())

    param = "-n" if platform.system() == "Windows" else "-c"

    resposta = subprocess.run(
        ["ping", param, "1", "google.com"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if resposta.returncode == 0:
        internet = "OK"
    else:
        internet = "Sem conexão"

    return ip, internet
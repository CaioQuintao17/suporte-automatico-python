import os
import platform

def coletar_sistema():
    usuario = os.environ.get("USERNAME") or os.environ.get("USER")
    computador = platform.node()
    sistema = platform.system() 
    
    return usuario, computador, sistema


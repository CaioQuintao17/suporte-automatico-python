def gerar_relatorio(usuario, computador, sistema, ip, internet, diagnostico):
    with open("relatorio.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(f"Usuário: {usuario}\n")
        arquivo.write(f"Computador: {computador}\n")
        arquivo.write(f"Sistema: {sistema}\n")
        arquivo.write(f"IP: {ip}\n")
        arquivo.write(f"Internet: {internet}\n")
        arquivo.write(f"Diagnóstico: {diagnostico}\n")
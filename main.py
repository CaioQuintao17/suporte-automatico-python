from sistema import coletar_sistema
from rede import coletar_rede
from relatorio import gerar_relatorio

usuario, computador, sistema = coletar_sistema()
ip, internet = coletar_rede()

if internet == "OK":
    diagnostico = "Sistema funcionando normalmente ✅"
else:
    diagnostico = "Sem conexão com a internet ❌\nSugestão: Verifique o Wi-Fi ou cabo de rede"

print("Usuário:", usuario)
print("Computador:", computador)
print("Sistema:", sistema)
print("IP:", ip)
print("Internet:", internet)
print("Diagnóstico:", diagnostico)

gerar_relatorio(usuario, computador, sistema, ip, internet, diagnostico)
#  Sistema de Suporte Técnico Automatizado em Python

Projeto desenvolvido para simular uma ferramenta de suporte técnico nível 1, capaz de coletar informações do sistema, diagnosticar conectividade de rede e gerar relatórios automáticos.

---

##  Objetivo do Projeto

Este sistema tem como objetivo automatizar tarefas básicas de suporte técnico, como:

- Coleta de informações do computador do usuário
- Verificação de conectividade com a internet
- Diagnóstico automático de status do sistema
- Geração de relatórios em arquivo `.txt`

---

##  Funcionalidades

###  Coleta de Sistema
- Usuário logado
- Nome do computador
- Sistema operacional

###  Diagnóstico de Rede
- Identificação do IP da máquina
- Teste de conectividade com a internet (ping)

###  Diagnóstico Inteligente
- Identifica se há conexão com a internet
- Gera sugestões automáticas em caso de falha

###  Geração de Relatório
- Criação automática de arquivo `.txt`
- Registro completo das informações coletadas

---

##  Estrutura do Projeto

```bash
suporte-automatico-python/
│
├── main.py            # Arquivo principal (orquestra o sistema)
├── sistema.py        # Coleta informações do sistema
├── rede.py           # Diagnóstico de rede e internet
├── relatorio.py      # Geração do relatório .txt



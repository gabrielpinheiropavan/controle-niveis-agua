
from colorama import Fore, Style, init

# Inicializa o Colorama
init()

# Lista com os níveis do reservatório
niveis = [
    {"nivel": 1, "situacao": "Muito baixo (CRÍTICO)"},
    {"nivel": 2, "situacao": "Baixo"},
    {"nivel": 3, "situacao": "Médio"},
    {"nivel": 4, "situacao": "Alto"},
    {"nivel": 5, "situacao": "Muito alto (ALERTA)"}
]


# Função responsável por definir a cor de cada nível
def definir_cor(nivel):

    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


# Exibição do monitoramento
print("=== MONITORAMENTO DO RESERVATÓRIO ===\n")

for item in niveis:
    cor = definir_cor(item["nivel"])

    mensagem = f"Nível {item['nivel']}: {item['situacao']}"

    print(cor + mensagem + Style.RESET_ALL)

print("\n=== MONITORAMENTO FINALIZADO ===")

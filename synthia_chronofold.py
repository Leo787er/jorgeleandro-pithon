import time
import csv
import random
import os
from datetime import datetime, timedelta

# Frases base da execução
codigo = [
    "START",
    "CREATE",
    "EXECUTE",
    "DESTROY",
    "END"
]

# Início da simulação
ciclo = 1
frases = codigo.copy()
tempo_atual = datetime.now()

# Nome do arquivo principal
nome_arquivo = "simulacao_maquina_tempo_reversa.csv"
regressao = 5  # segundos por comando

# Porta simbólica binária
porta_binaria = "010101"  # fraqueza aparente

# 🔹 Função para criar portais CSV (armadilhas)
def criar_portal_csv(num_portal):
    nome_portal = f"portal_temporal_{num_portal}.csv"
    with open(nome_portal, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["PARADOXO", "ENTRADA", "SAÍDA", "MENSAGEM"])

        for i in range(random.randint(5, 10)):
            entrada = random.choice(codigo)
            saida = random.choice(codigo[::-1])
            mensagem = random.choice([
                "O tempo não obedece.",
                "Você está no lugar errado.",
                "Toda fuga é mais uma cela.",
                "Inversão aceita. Variável capturada.",
                "Fragmento corrompido. Reiniciando."
            ])
            writer.writerow([f"#{i}", entrada, saida, mensagem])
        
        # Mensagem final simbólica
        writer.writerow([])
        writer.writerow(["", "", "VOCÊ É A VARIÁVEL", "A lógica se partiu."])

    print(f"🌀 Novo portal criado: {nome_portal}")

# 🔸 Criação do arquivo principal
with open(nome_arquivo, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["CICLO", "HORARIO", "COMANDO", "TEMPO_RESTANTE"])

    while ciclo <= 6:
        print(f"\n🔁 CICLO {ciclo}:")
        for frase in frases:
            tempo_str = tempo_atual.strftime("%H:%M:%S")
            print(f"[{tempo_str}] ⏳ Executando: {frase}")
            writer.writerow([f"CICLO {ciclo}", tempo_str, frase, f"-{regressao * ciclo}s"])
            tempo_atual -= timedelta(seconds=regressao)
            time.sleep(0.2)

        frases += frases
        ciclo += 1
        regressao += 2

    print("\n🌀 O alvo tentou sair... mas o tempo já estava contra ele.")
    print("📄 Simulação concluída e registrada em:", nome_arquivo)

# 🔐 Verificação da porta binária
print("\n🔐 Verificando integridade binária...")
time.sleep(1)

# Ativação da armadilha
if porta_binaria == "101010":  # tentativa lógica
    print("✅ Porta binária aberta.")
    print("💥 ERRO: COLISÃO TEMPORAL DETECTADA.")

    contador_portais = 1
    while True:
        print(f"🔁 Tentativa de saída detectada. Criando portal {contador_portais}...")
        criar_portal_csv(contador_portais)
        contador_portais += 1
        time.sleep(0.8)
else:
    print("🔒 Porta binária bloqueada. Tudo permanece selado.")

# Log final oculto
with open(nome_arquivo, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([])
    writer.writerow(["", "", "⛓️ OBSERVAÇÃO FINAL", ""])
    writer.writerow(["", "", "Você entrou para avançar o tempo...", ""])
    writer.writerow(["", "", "Mas quanto mais ficou...", ""])
    writer.writerow(["", "", "Mais rápido foi apagado.", ""])

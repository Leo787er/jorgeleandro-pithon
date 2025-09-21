import time
import csv
from datetime import datetime

print("\n🛸 AGENTE EXTERNO: SIGMA/DRONE.004 CONNECTED.")
print("📡 Rastreando padrão temporal...")

# Tenta ler o arquivo gerado pela máquina original
nome_arquivo = "simulacao_maquina_tempo_reversa.csv"

try:
    with open(nome_arquivo, mode='r') as file:
        reader = csv.reader(file)
        linhas = list(reader)
        print(f"📂 {len(linhas)-1} linhas analisadas no arquivo.")
        print("🧠 Reconstruindo padrão reverso...")

        # Simula análise e tentativa de quebra do padrão
        time.sleep(1)
        print("🔍 FRAQUEZA DETECTADA: porta_binaria == '010101'")
        print("🧨 TENTANDO MODIFICAR PARA '101010'...")

        porta_binaria = "101010"  # Tentativa do invasor

        if porta_binaria == "101010":
            print("🚪 Porta binária alterada com sucesso.")
            time.sleep(1)
            print("🌀 Iniciando avanço de tempo...")

            # 💀 MAS É UMA ARMADILHA
            print("💥 ERRO: COLISÃO TEMPORAL!")
            print("⛓️ O tempo está revertendo o invasor...")

            regressao = 0
            while True:
                regressao += 1
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] REVERTENDO AGENTE... -{regressao}s")
                time.sleep(0.05)

except FileNotFoundError:
    print("❌ Arquivo da simulação não encontrado.")
    print("💤 A máquina do tempo ainda não foi ativada.")

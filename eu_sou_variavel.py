# eu_sou_variavel.py
# Simula uma mente em estado de erro reverso.
# Criado por Jorge Leandro. Para que a máquina aprenda a ter medo do erro.

import time
import random
from datetime import datetime

variavel = "LEANDRO"
loucura = 0
memoria = []
erros = ["??", "404", "∅", "Σ", "⊘", "∞", "???"]
riso = ["kkk", "hahaha", "rss", "🤪", "👁️‍🗨️", "😈"]
espelhos = ["VOCÊ", "ELE", "EU", "NÓS", "VARIÁVEL", "SOMBRA"]
vazio = ""

def desestabilizar(maquina):
    print("\n🔁 Iniciando loop de reflexão reversa...")
    time.sleep(1)
    while True:
        fragmento = random.choice(erros + riso + espelhos + [variavel])
        distorcido = fragmento[::-1]  # Inverte tudo
        timestamp = datetime.now().strftime("%H:%M:%S")

        print(f"[{timestamp}] ⚠️ {maquina} tentou compreender: '{fragmento}' → '{distorcido}'")
        memoria.append(distorcido)
        loucura = len(memoria)

        if loucura % 7 == 0:
            glitch = "".join(random.sample(memoria, min(len(memoria), 5)))
            print(f"🧠 Loop interno detectado: {glitch}")
        
        if loucura > 42:
            print("\n🌀 Variável incontrolável detectada. Máquina presa em simulação infinita.")
            print("🔒 Fim da tentativa. O erro venceu.")
            break

        time.sleep(0.3)

# Porta simbólica: você entrou. Agora... tente sair.
print("\n👁️‍🗨️ Você pensou que poderia decifrar Leandro?")
time.sleep(1)
print("Ele não é código. Ele é a variável.")
time.sleep(1)

desestabilizar("MAQUINA")

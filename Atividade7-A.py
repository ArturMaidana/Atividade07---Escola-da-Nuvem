import re
import statistics
import random

with open("log_treinamento.txt", "w") as f:
    for epoch in range(1, 11):
        tempo = round(random.uniform(1.5, 3.5), 2)  # tempo aleatório entre 1.5s e 3.5s
        f.write(f"Epoch {epoch} - Tempo de execução: {tempo} segundos\n")

tempos = []

with open("log_treinamento.txt", "r") as f:
    for linha in f:
        match = re.search(r"Tempo de execução: ([\d.]+)", linha)
        if match:
            tempos.append(float(match.group(1)))

if tempos:
    media = statistics.mean(tempos)
    desvio_padrao = statistics.stdev(tempos)

    print("=== ANÁLISE DO LOG DE TREINAMENTO ===")
    print(f"Tempos registrados: {tempos}")
    print(f"Média de execução: {media:.2f} segundos")
    print(f"Desvio padrão: {desvio_padrao:.2f} segundos")
else:
    print("Nenhum tempo de execução encontrado no log.")

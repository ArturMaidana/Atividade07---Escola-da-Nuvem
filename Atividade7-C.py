import csv

print("=== LEITURA DO ARQUIVO CSV ===")

try:
    with open("pessoas.csv", "r", encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for i, linha in enumerate(leitor):
            if i == 0:
                print(f"{linha[0]:<10} | {linha[1]:<5} | {linha[2]}")
                print("-" * 35)
            else:
                print(f"{linha[0]:<10} | {linha[1]:<5} | {linha[2]}")
except FileNotFoundError:
    print("Arquivo 'pessoas.csv' não encontrado. Execute o script anterior primeiro.")

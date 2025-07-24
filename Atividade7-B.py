import csv

pessoas = [
    ["Nome", "Idade", "Cidade"],
    ["Artur", 22, "Cuiabá"],
    ["Marina", 25, "São Paulo"],
    ["João", 30, "Rio de Janeiro"],
    ["Ana", 28, "Fortaleza"]
]

with open("pessoas.csv", "w", newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo)
    writer.writerows(pessoas)

print("Arquivo 'pessoas.csv' criado com sucesso!")

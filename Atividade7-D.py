import json

pessoa = {
    "nome": "Artur Maidana",
    "idade": 22,
    "cidade": "Cuiabá"
}

with open("pessoa.json", "w", encoding='utf-8') as f:
    json.dump(pessoa, f, indent=4, ensure_ascii=False)

print("Arquivo 'pessoa.json' criado com os dados da pessoa.")

with open("pessoa.json", "r", encoding='utf-8') as f:
    dados_lidos = json.load(f)

print("\n=== DADOS LIDOS DO JSON ===")
print(f"Nome: {dados_lidos['nome']}")
print(f"Idade: {dados_lidos['idade']}")
print(f"Cidade: {dados_lidos['cidade']}")

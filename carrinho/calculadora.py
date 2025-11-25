# carrinho/calculadora.py

produtos_padrao = [
    {"codigo": 101, "nome": "Café Gourmet",       "valor": 25.50, "qtd": 2},
    {"codigo": 102, "nome": "Filtro de Papel",    "valor": 5.00,  "qtd": 5},
    {"codigo": 103, "nome": "Açúcar Mascavo",     "valor": 12.00, "qtd": 1},
    {"codigo": 104, "nome": "Caneca Premium",     "valor": 45.00, "qtd": 3},
    {"codigo": 105, "nome": "Biscoito",           "valor": 8.90,  "qtd": 4},
]


def calcular_total_base(lista_produtos):
    total = 0
    for p in lista_produtos:
        total += p["valor"] * p["qtd"]
    return round(total, 2)


def calcular_total_carrinho(total_base, forma_pagamento):
    regras = {
        "PIX": 0.90,              # 10% de desconto
        "DEBITO": 1.00,           # sem alteração
        "CREDITO": 1.05           # 5% de juros
    }

    forma_pagamento = forma_pagamento.upper()

    if forma_pagamento not in regras:
        raise ValueError("Forma de pagamento inválida")

    return round(total_base * regras[forma_pagamento], 2)

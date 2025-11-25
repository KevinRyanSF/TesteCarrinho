# tests/test_calculadora.py
import pytest
from carrinho.calculadora import calcular_total_base, calcular_total_carrinho, produtos_padrao


def test_total_base_padrao():
    assert calcular_total_base(produtos_padrao) == 258.60


@pytest.mark.parametrize(
    "forma_pagamento, esperado",
    [
        ("PIX", 232.74),
        ("DEBITO", 258.60),
        ("CREDITO", 271.53),
    ]
)
def test_calcular_total_carrinho(forma_pagamento, esperado):
    total_base = calcular_total_base(produtos_padrao)
    resultado = calcular_total_carrinho(total_base, forma_pagamento)
    assert resultado == esperado

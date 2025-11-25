# main.py
from carrinho.calculadora import calcular_total_base, calcular_total_carrinho, produtos_padrao

total = calcular_total_base(produtos_padrao)

print("Total base:", total)
print("PIX:", calcular_total_carrinho(total, "PIX"))
print("Débito:", calcular_total_carrinho(total, "debito"))
print("Crédito:", calcular_total_carrinho(total, "credito"))

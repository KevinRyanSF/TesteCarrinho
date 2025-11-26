# Grupo: Gabriel, Kevin, Luiz, Thiago e Ryan

Cenário:
Você foi contratado(a) para desenvolver a lógica de totalização de um carrinho de compras online. O carrinho contém uma lista de produtos e o valor final deve ser ajustado com base na forma de pagamento selecionada pelo cliente. O objetivo principal deste exercício é aplicar e testar a função de cálculo utilizando .
Dados de Entrada (Carrinho Padrão)
O carrinho inicial é composto pelos 5 produtos listados abaixo:

Código  Nome do Produto   Valor Unitário (R$)  Quantidade
101       Café Gourmet          25.50             2
102       Filtro de Papel       5.00              5
103       Açúcar Mascavo        12.00             1
104       Caneca Premium        45.00             3
105       Biscoito              8.90              4
O valor total base (sem considerar descontos ou juros) para este carrinho é de .
Regras de Negócio (Ajuste por Forma de Pagamento)
O valor total do carrinho deve ser ajustado de acordo com as seguintes regras de pagamento: Aplica-se um sobre o valor total base. há aplicação de desconto ou juros (fator 0%). Aplica-se sobre o valor total base.
TAREFA DO EXERCÍCIO Crie uma função chamada calcular_total_carrinho que aceite a lista de produtos (ou o total base) e a forma de pagamento como entrada, e retorne o valor total final ajustado. Utilizando um framework de testes (como pytest), crie um conjunto de testes que utilize a parametrização para verificar se a função calcular_total_carrinho retorna o valor esperado para .Resultados Esperados para o Carrinho Padrão

Forma de Pagamento

Cálculo
Resultado Esperado (R$)   
PIX  258.60 * 0.90  =  232.74
Cartão de Débito 258.60 * 1.00 = 258.60
Cartão de Crédito  258.60 * 1.05 = 271.53

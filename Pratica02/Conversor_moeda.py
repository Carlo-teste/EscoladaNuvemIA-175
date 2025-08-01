"""
1- Conversor de Moeda 

Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""
# Dados fornecidos
valor_em_reais = 100.00
taxa_dolar = 5.60
taxa_euro = 6.60

# Conversões
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

# Exibição dos resultados
print("=== CONVERSOR DE MOEDA ===")
print(f"Valor em reais: R$ {valor_em_reais:.2f}")
print(f"Valor em dólares: US$ {valor_em_dolares:.2f}")
print(f"Valor em euros: € {valor_em_euros:.2f}")
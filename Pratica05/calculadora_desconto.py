"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do 
preço final após a aplicação do desconto. Requisitos:
    - Permitir que o usuário informe o preço do produto e o percentual de desconto.
    - Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
    - Exibir o preço final com duas casas decimais para garantir precisão. 
    Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""
while True:
    try:
        # Solicita o valor do produto
        preco = float(input("Digite o preço do produto (ex: 250.75): "))

        # Solicita o percentual de desconto
        desconto = float(input("Digite o percentual de desconto (ex: 10 para 10%): "))

        # Verifica se os valores são válidos (não negativos)
        if preco < 0 or desconto < 0:
            print("Erro: valores negativos não são permitidos. Tente novamente.\n")
            continue

        # Calcula o valor do desconto
        valor_desconto = preco * (desconto / 100)

        # Calcula o preço final com desconto aplicado
        preco_final = preco - valor_desconto

        # Mostra os resultados formatados
        print("\n=== RESUMO DA COMPRA ===")
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Desconto aplicado: {desconto}% → R$ {valor_desconto:.2f}")
        print(f"Preço final com desconto: R$ {preco_final:.2f}")
        break  # Encerra o loop após uma entrada válida

    except ValueError:
        print("Erro: entrada inválida. Digite apenas números válidos (use ponto, não vírgula).\n")

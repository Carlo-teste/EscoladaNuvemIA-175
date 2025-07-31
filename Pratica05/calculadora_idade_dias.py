"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade aproximada em dias, com base no ano de nascimento.

    Parâmetro:
        ano_nascimento (int): o ano em que a pessoa nasceu.

    Retorna:
        int: idade aproximada em dias.
    """
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    return idade * 365  # Aproximação sem considerar anos bissextos


# Parte interativa
while True:
    try:
        entrada = input("Digite o ano de nascimento (ex: 1990) ou 'fim' para encerrar: ")

        if entrada.lower() == 'fim':
            print("Programa encerrado.")
            break

        ano = int(entrada)

        ano_atual = date.today().year
        if ano > ano_atual or ano < 1900:
            print("Ano inválido. Digite um ano entre 1900 e o ano atual.\n")
            continue

        idade_dias = calcular_idade_em_dias(ano)
        print(f"Você tem aproximadamente {idade_dias} dias de vida.\n")
        break

    except ValueError:
        print("Entrada inválida. Por favor, digite um ano numérico válido.\n")

"""
6- Calculadora de Comissão

Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.

"""
# Entrada de dados
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo (R$): "))
total_vendas = float(input("Digite o total de vendas no mês (R$): "))

# Cálculo da comissão (15% sobre o total de vendas)
comissao = total_vendas * 0.15

# Cálculo do total a receber
total_receber = salario_fixo + comissao

# Saída formatada com duas casas decimais
print(f"TOTAL = R$ {total_receber:.2f}")

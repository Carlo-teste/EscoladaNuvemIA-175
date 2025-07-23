"""
4- Calculadora de Consumo de Combustível

 Desenvolva um programa que calcula o consumo médio de 
 combustível de um veículo. Use os seguintes dados:

 - Distância percorrida: 300 km
 - Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e exibir 
todos os dados da viagem, incluindo o resultado final 
arredondado para duas casas decimais.
"""

# Dados da Viagem
distancia_percorrida = 277 # em Km 
combustivel_gasto = 25 # litros

consumo_medio = distancia_percorrida / combustivel_gasto

print("Dados da Viagem")
print(f"Distância percorrida: {distancia_percorrida} Km")
print(f"Combustível gasto: {combustivel_gasto} litros")
print(f"O consumo médio foi de: {consumo_medio:.2f} Km/l")
#print("O consumo médio foi de:", round(consumo_medio, 2), "litros")

print("=== Conversor de Temperatura ===")
# Entrada do usuário
temperatura = float(input("Digite o valor da temperatura: "))
origem = input("Digite a unidade de origem ('C'elsius, 'F'ahrenheit ou 'K'elvin): ").lower()
destino = input("Digite a unidade de destino ('C'elsius, 'F'ahrenheit ou 'K'elvin): ").lower()
if origem == "c":
    origem = "celsius"
elif origem == "f":
    origem = "fahrenheit"
elif origem == "k":
    origem = "kelvin"
if destino == "c":
    destino = "celsius"
elif destino == "f":
    destino = "fahrenheit"
elif destino == "k":
    destino = "kelvin"
print(f"\n...CONVERTENDO {temperatura}º {origem.capitalize()} PARA {destino.capitalize()}")
# Conversão
if origem == destino:
    resultado = temperatura
elif origem == "celsius" or "c" and destino == "fahrenheit" or "f":
    resultado = (temperatura * 9/5) + 32
elif origem == "celsius" or "c" and destino == "kelvin" or "k":
    resultado = temperatura + 273.15
elif origem == "fahrenheit" or "f" and destino == "celsius" or "c":
    resultado = (temperatura - 32) * 5/9
elif origem == "fahrenheit" or "f" and destino == "kelvin" or "k":
    resultado = (temperatura - 32) * 5/9 + 273.15
elif origem == "kelvin" or "k" and destino == "celsius" or "c":
    resultado = temperatura - 273.15
elif origem == "kelvin" or "k" and destino == "fahrenheit" or "f":
    resultado = (temperatura - 273.15) * 9/5 + 32
else:
    resultado = None
    print("Unidade inválida. Certifique-se de digitar: Celsius, Fahrenheit ou Kelvin.")
# Exibe o resultado
if resultado is not None:
    print(f"\n{temperatura} {origem.capitalize()} = {resultado:.2f}º {destino.capitalize()}")
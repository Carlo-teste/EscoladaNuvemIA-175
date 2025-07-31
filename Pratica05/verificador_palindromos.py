"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando
espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""
import string

def eh_palindromo(texto: str) -> str:
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

while True:
    entrada = input("Digite uma palavra ou frase (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        print("Programa encerrado.")
        break

    resultado = eh_palindromo(entrada)
    print(f"É palíndromo? {resultado}\n")

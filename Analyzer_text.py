texto = input("Digite o texto a ser analisado: ")

texto = texto.lower()
texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.replace("!", "")
texto = texto.replace("?", "")
texto = texto.replace(";", "")
texto = texto.replace(":", "")
texto = texto.replace("(", "")
texto = texto.replace(")", "")
texto = texto.replace("[", "")
texto = texto.replace("]", "")
texto = texto.replace("{", "")
texto = texto.replace("}", "")

palavras = texto.split()

total_palavras = len(palavras)
total_caracteres = len(texto)

frequencia_palavras = {}
for palavra in palavras:
    if palavra in frequencia_palavras:
        frequencia_palavras[palavra] += 1
    else:
        frequencia_palavras[palavra] = 1

print("Estatísticas do texto:")
print("-" * 20)
print(f"Total de palavras: {total_palavras}")
print(f"Total de caracteres: {total_caracteres}")
print("-" * 20)
print("Frequência de cada palavra:")
for palavra, frequencia in frequencia_palavras.items():
    print(f"{palavra}: {frequencia}")

# Variáveis iniciais
palavras = ["Gama", "Matematica", "Vestibular", "IA"]
caractere = "a"

# Ordenando a lista a partir da quantidade de caracteres encontrados
palavras.sort(key=lambda palavra: palavra.lower().count(caractere),
              reverse=True)

# Mostrando resultado
print(palavras)

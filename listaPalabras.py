palabras = input("Ingresa la lista de palabras: ")
palabras_lista = palabras.split(",")
letra = input("Ingresa la letra con la que deben comenzar las palabras: ")
palabras_filtradas = [palabra for palabra in palabras if palabra.lower().startswith(letra.lower())]
print("Palabras que comienzan con la letra", letra + ":")
for palabra in palabras_filtradas:
    print(palabra)



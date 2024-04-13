palabra = input("Por favor, ingresa una palabra o frase: ")
palabra = palabra.lower()

conteo_a = 0
conteo_e = 0
conteo_i = 0
conteo_o = 0
conteo_u = 0

for letra in palabra:
    if letra == 'a':
        conteo_a += 1
    elif letra == 'e':
        conteo_e += 1
    elif letra == 'i':
        conteo_i += 1
    elif letra == 'o':
        conteo_o += 1
    elif letra == 'u':
        conteo_u += 1

print(f"La vocal 'a' aparece {conteo_a} veces.")
print(f"La vocal 'e' aparece {conteo_e} veces.")
print(f"La vocal 'i' aparece {conteo_i} veces.")
print(f"La vocal 'o' aparece {conteo_o} veces.")
print(f"La vocal 'u' aparece {conteo_u} veces.")

### 🟡 C7 — Contador de palabras
#Dada una frase cualquiera, armá un diccionario que cuente cuántas veces aparece cada palabra.
#**Listo cuando:** el diccionario tiene una clave por palabra distinta y el número correcto de apariciones.

frase = "hola mundo hola python mundo hola"

palabras = frase.split()
contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] = contador[palabra] + 1
    else:
       contador[palabra] = 1

print(contador)
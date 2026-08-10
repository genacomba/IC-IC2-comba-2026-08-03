### 🟡 B7 — Sin repetidos
#Dada la lista `[3, 5, 3, 8, 5, 1, 8, 8]`, obtené una lista de los valores **sin repetir**. Investigá `set()`.
#**Listo cuando:** no quedan duplicados. El orden no importa y **no tiene por qué coincidir con el de tu compañero** — `set()` no garantiza ningún orden particular, eso es normal.

lista= [3, 5, 3, 8, 5, 1, 8, 8]

sin_repetidos = list(set(lista))
print(sin_repetidos)

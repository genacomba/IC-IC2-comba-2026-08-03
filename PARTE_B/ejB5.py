### 🔴 B5 — Ranking
#Dada una lista de puntajes, imprimila **ordenada de mayor a menor**. Investigá cómo ordenar una lista en Python.
#**Listo cuando:** sale ordenada y entendés la diferencia entre ordenar la lista en su lugar y obtener una copia ordenada.

puntajes = [120, 45, 300, 80, 210]

ranking = sorted(puntajes, reverse=True)

print("Original:", puntajes)
print("Ranking:", ranking)
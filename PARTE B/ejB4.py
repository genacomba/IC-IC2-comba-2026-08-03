### 🟡 B4 — Filtrar
#De la lista `[120, 45, 300, 80, 210]`, armá una **lista nueva** solo con los puntajes mayores a 100.
#**Listo cuando:** la lista nueva tiene `[120, 300, 210]` y la original quedó intacta.

puntajes = [120, 45, 300, 80, 210]

mayores= []

for puntaje in puntajes:
    if puntaje > 100:
        mayores.append(puntaje)

print(puntajes)
print(mayores)
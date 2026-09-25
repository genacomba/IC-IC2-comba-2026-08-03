### 🔴 B8 — Promedio móvil
#Dada una lista de 10 lecturas cualquiera, calculá el **promedio de a 3 elementos consecutivos** (posiciones 0-1-2, después 1-2-3, después 2-3-4…). Esto se llama ventana deslizante.
#**Listo cuando:** la lista de promedios tiene 2 elementos menos que la original y podés explicar por qué.

lecturas = [5,10,15,20,25,30,35,40,45,50]

promedios = []

for i in range(0,8):
    promedio = (lecturas[i] + lecturas[i+1] + lecturas[i+2]) / 3
    promedios.append(promedio)

print(promedios)

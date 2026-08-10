### 🔴 A7 — Cadena de conversiones
#Encadená conversiones de unidades: de kilómetros a millas, y de millas a pies (buscá los factores de conversión). Escribí el camino completo `km → millas → pies` para un valor cualquiera, sin escribir tres scripts sueltos.
#**Listo cuando:** podés cambiar el valor de entrada una sola vez y las tres conversiones se actualizan solas.

km = float(input("Distancia en kilometros: "))

millas = km / 1.609
pies = millas * 5280

print("Millas: ", round(millas,2), "Pies: ", round(pies, 2))
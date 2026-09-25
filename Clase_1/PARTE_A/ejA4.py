### 🟡 A4 — Redondeo y formato
#Mostrá el promedio de A1 con **un solo decimal** (ej. `7.2`, no `7.200000001`).
#**Listo cuando:** la salida tiene exactamente un decimal.
notas = [7,4,9,10,6]
total= 0 
for nota in notas:
    total = total + nota

promedio = total /5

if promedio >= 6:
    print(f"Promedio: {promedio:.1f} Aprobado")
else:
    print(f"Promedio: {promedio:.1f} Desaprobado")
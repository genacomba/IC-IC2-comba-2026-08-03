### 🟢 A1 — Calculadora de promedio
#Tenés las notas de un alumno: `7, 4, 9, 10, 6`. Calculá e imprimí el promedio. Después imprimí si **aprobó** (promedio ≥ 6) o no.
#**Listo cuando:** imprime el promedio correcto y el cartel de aprobado/desaprobado.

notas = [7,4,9,10,6]
total= 0 
for nota in notas:
    total = total + nota

promedio = total /5

if promedio >= 6:
    print("Promedio:", promedio, "Aprobado")
else:
    print("Promedio:", promedio, "Desaprobado")




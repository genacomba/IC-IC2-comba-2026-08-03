### 🟡 A6 — Par, impar, y turnos
#Tenés 30 alumnos numerados del 1 al 30. Usando el operador `%` (módulo), separalos en dos grupos: los de número par y los de número impar. Imprimí cuántos hay en cada grupo.
#**Listo cuando:** los dos grupos suman 30 y entendés qué hace `%` (no es una división normal)

pares = 0 
impares = 0

for alumno in range (1,31):
    if alumno % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

total = pares + impares
print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Total: {total}")

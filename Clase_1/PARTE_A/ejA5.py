### 🟢 A5 — ¿Mayor o menor de edad?
#Dada una variable `edad`, imprimí `"mayor de edad"` o `"menor de edad"` según corresponda. Probalo con `17`, `18` y `0`.
#**Listo cuando:** el caso límite (`18`) da el resultado correcto sin que lo hayas mirado dos veces.

edad = int(input("Ingresar tu edad: "))

if edad >= 18:
    print("Mayor de edad")
else: 
    print("Menor de edad")
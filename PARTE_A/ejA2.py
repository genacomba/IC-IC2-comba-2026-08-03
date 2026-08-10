### 🟢 A2 — El tipo importa
#Creá una variable `cantidad = "5"` (con comillas) y otra `precio = 100`. Hacé `cantidad * precio` e imprimí el resultado — **no da un error**, pero tampoco da lo que uno esperaría de una multiplicación. Después arreglalo para que dé `500`.
#**Listo cuando:** entendés *por qué* `"5" * 100` no explota pero tampoco multiplica, y por qué la versión arreglada sí da `500`. (Pista: `type(cantidad)`.)

cantidad = "5"
precio = 100

cantidad = int(cantidad)
total = cantidad * precio

print(total)


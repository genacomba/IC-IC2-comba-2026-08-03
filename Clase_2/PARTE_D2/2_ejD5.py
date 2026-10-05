#🔴 D5 — Diseñá tus topics
#Pensá un esquema de topics para una casa con 3 ambientes y 2 tipos de sensor cada uno. Justificá la jerarquía. Listo cuando: tu esquema permite suscribirse "a todo", "a un ambiente" y "a un tipo de sensor" usando wildcards.




#Para una casa con tres ambientes (cocina, dormitorio y living) y dos tipos de sensores (temperatura y humedad), usaría la jerarquía `casa/ambiente/sensor`.

#Los topics serían `casa/cocina/temperatura`, `casa/cocina/humedad`, `casa/dormitorio/temperatura`, `casa/dormitorio/humedad`, `casa/living/temperatura` y `casa/living/humedad`.

#Esta jerarquía permite suscribirse a toda la casa con `casa/#`, a un ambiente con `casa/cocina/#` y a un tipo de sensor en todos los ambientes con `casa/+/temperatura`.#

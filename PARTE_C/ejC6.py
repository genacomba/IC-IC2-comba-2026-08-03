### 🟢 C6 — Combinar fichas
#Tenés dos diccionarios de la misma película con datos distintos, ej. `{"titulo": "Dune", "anio": 2021}` y `{"puntaje": 8, "anio": 2024}`. Combinalos en uno solo. ¿Qué pasa con `anio`, que está en los dos? Investigá `.update()` o el operador `|`.
#**Listo cuando:** entendés qué valor "gana" cuando una clave se repite — y que depende del **orden** en que combines los diccionarios (`dict1 | dict2` no da lo mismo que `dict2 | dict1`; con `.update()` pasa lo mismo según a cuál le hacés `.update()` de cuál). No hay una única respuesta "correcta" de qué año queda, lo importante es que sepas explicar por qué quedó ese.

dict1 = {
    "titulo": "Dune",
    "anio": 2021
}

dict2 = {
    "puntaje": 8,
    "anio": 2024
}

dict1.update(dict2)
print(dict1)
### 🔴 C8 — Diccionario anidado
#Armá un "inventario de tienda": un diccionario donde cada clave es un producto y el valor es *otro diccionario* con `precio` y `stock`. Accedé al precio de un producto específico sin recorrer nada, solo encadenando claves.
#**Listo cuando:** llegás al dato con `inventario["producto"]["precio"]` y entendés por qué es un dict "de dos pisos".

inventario = {
    "manzana": {
        "precio" : 10,
        "stock" : 5
    },
    "banana" : {
        "precio" : 5,
        "stock" : 2
    },
    "pera": {
        "precio": 15,
        "stock": 10
    
    }
}
print(inventario["banana"]["precio"])
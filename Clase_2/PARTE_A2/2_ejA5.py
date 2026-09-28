### 🟢 A5 — Idempotencia
#Un pedido es **idempotente** si hacerlo una vez o cien veces seguidas deja el mismo resultado. De GET, POST, PUT y DELETE, ¿cuáles son idempotentes y cuáles no? Pensá qué pasa si un mismo POST de "crear libro" se manda dos veces por un error de red. **Listo cuando:** identificás por qué POST normalmente NO es idempotente (crea un libro nuevo cada vez) y PUT sí (reemplaza siempre por lo mismo).



#GET: idempotente, porque leer un recurso varias veces no lo modifica.
#POST: no idempotente, porque cada vez que se envía puede crear un nuevo recurso. Por ejemplo, si se manda dos veces el mismo POST para crear un libro, se pueden crear dos libros.
#PUT: idempotente, porque reemplaza el recurso por los mismos datos. Aunque se envíe varias veces, el resultado final es el mismo.
#DELETE: idempotente, porque una vez eliminado el recurso, repetir la operación no cambia el estado final.

#Por lo tanto, GET, PUT y DELETE son idempotentes, mientras que POST no lo es.

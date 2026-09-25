#🟢 A2 — Leer códigos de estado
#¿Qué significa cada uno y cuándo lo devolverías? 200, 201, 204, 400, 404, 405, 422, 500. Listo cuando: das un ejemplo concreto de cada uno, en el dominio de libros.


#200) La operación salió correctamente y hay una respuesta. Ej: GET /libros devuelve la lista de libros
#201) Se creó correctamente un recurso nuevo. Ej: POST /libros crea un libro
#204) La operación salió bien, pero no hay contenido para devolver. Ej: DELETE /libros/5 elimina el libro y no devuelve nada
#400) El pedido está mal formado. Ej: El cliente manda un body que no es JSON válido
#404) El recurso que se pidió no existe. Ej: GET /libros/99 pero no existe el libro 99
#405) La URL existe, pero ese método no está permitido. Ej: Existe /libros, pero hacemos DELETE /libros cuando ese endpoint no permite DELETE
#422) El pedido se entiende, pero los datos no cumplen lo esperado. Ej: Enviamos un libro sin titulo, cuando la API exige ese campo
#500) Ocurrió un error interno en el servidor. Ej: Nuestro código tiene un error y se rompe mientras procesa el pedido

#🟢 A6 — Headers, lo mínimo

#¿Para qué sirve el header Content-Type: application/json? ¿Qué pasaría si un cliente manda un body JSON sin ese header? Listo cuando: explicás con tus palabras que el header le dice al servidor cómo interpretar el body, no es decorativo.




#El header le indica al servidor que el contenido del body está en formato JSON y cómo debe interpretarlo.
#Si un cliente manda un body en formato JSON sin ese header, el servidor puede no reconocer que los datos están en JSON y puede rechazar la petición o interpretarla incorrectamente.
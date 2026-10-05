#🟡 D3 — Pub/sub vs request/response
#Escribí en 3 o 4 líneas la diferencia entre "pedir y que te contesten" (la API que hiciste hoy) y "publicar y que el que quiera escuche" (MQTT). Dá un ejemplo donde convenga cada uno. Listo cuando: podés defender cuándo usar cada modelo.




#En una API, un cliente hace una petición y espera una respuesta del servidor. Por ejemplo, una aplicación puede pedir la información de un libro y la API se la devuelve.
#En MQTT, un cliente publica un mensaje en un topic y cualquier cliente que esté suscripto puede recibirlo, sin que el emisor tenga que saber quién lo está escuchando. Por ejemplo, sirve para enviar datos de sensores a varios dispositivos.

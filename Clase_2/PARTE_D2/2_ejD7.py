#🟡 D7 — Mensajes retenidos (retained)
#Investigá qué es un mensaje retained en MQTT: qué pasa cuando alguien se suscribe a un topic después de que se publicó, si ese mensaje se marcó como retenido. Listo cuando: explicás la diferencia con D2 (donde el que se suscribe tarde se pierde el mensaje) y quién se beneficiaría de un retained (pista: pensá en "cuál es el último estado conocido de un sensor").


#Un mensaje retained es un mensaje que el broker guarda como el último estado conocido de un topic. Si un cliente se suscribe después de que se publicó ese mensaje, el broker se lo entrega automáticamente.
#La diferencia con D2 es que un mensaje normal publicado cuando no hay suscriptores se pierde, mientras que un mensaje retained queda guardado para los próximos suscriptores.
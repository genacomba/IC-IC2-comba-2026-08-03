#🟡 D6 — QoS, la idea (sin implementarlo)
#MQTT tiene tres niveles de QoS (Quality of Service): 0 ("como salga, sin garantía"), 1 ("llega al menos una vez, puede duplicarse") y 2 ("llega exactamente una vez"). Investigá qué significa cada uno y pensá: para un sensor que publica la temperatura cada 2 segundos, ¿importa perder algún mensaje? ¿Y para un comando de "abrir la puerta"? Listo cuando: podés justificar qué QoS usarías para un dato que se repite seguido vs. un comando puntual que no puede perderse.




#QoS 0 envía el mensaje una sola vez y no garantiza que llegue. QoS 1 garantiza que llegue al menos una vez, aunque puede llegar duplicado. QoS 2 garantiza que el mensaje se entregue exactamente una vez, pero requiere mayor intercambio de mensajes.

#Para un sensor que publica la temperatura cada 2 segundos usaría QoS 0, porque perder una medición no es grave ya que pronto llegará otra. Para un comando puntual como “abrir la puerta” usaría QoS 1 o QoS 2, porque es importante que el comando no se pierda.
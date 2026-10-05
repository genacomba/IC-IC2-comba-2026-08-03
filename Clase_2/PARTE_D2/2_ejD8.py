#🔴 D8 — MQTT vs. preguntar todo el tiempo (polling)

#Una alternativa a MQTT sería que cada cliente le pregunte a la API "¿hay algo nuevo?" cada 1 segundo (esto se llama polling, y usa el modelo request/response que ya conocés). Comparalo con pub/sub: ¿qué pasa con la carga del servidor si hay 1000 sensores? ¿Y con la demora entre que pasa el evento y alguien se entera? Listo cuando: podés explicar con un ejemplo numérico (aunque sea aproximado) por qué pub/sub escala mejor que el polling para muchos sensores.


#Con polling, si hay 1000 sensores y cada uno consulta a la API cada 1 segundo, se generan aproximadamente 1000 consultas por segundo, aunque no haya ningún dato nuevo. En un minuto serían unas 60.000 consultas.
#Con MQTT, los sensores publican cuando tienen un dato o evento para enviar y el broker lo distribuye a los clientes suscriptos. Esto evita muchas consultas innecesarias y reduce la carga cuando hay muchos dispositivos.
#Además, con polling puede existir una demora de hasta casi 1 segundo si se consulta cada 1 segundo. Con MQTT, el mensaje se publica cuando ocurre el evento, por lo que el suscriptor puede recibirlo inmediatamente. Por eso pub/sub puede escalar mejor para muchos sensores.
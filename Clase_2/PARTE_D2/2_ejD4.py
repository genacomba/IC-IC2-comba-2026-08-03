#🟡 D4 — Topics y jerarquía
#Si un sensor de temperatura publica en casa/cocina/temp y uno de humedad en casa/cocina/hum, ¿a qué se suscribiría alguien que quiere todo lo de la cocina? Investigá los wildcards de MQTT (+ y #) y la diferencia entre ambos. Listo cuando: sabés qué es un wildcard, la diferencia entre + (un nivel) y # (todos los niveles restantes), y cuándo usar cada uno. (Vas a usar esto de verdad en la clase 3.)


#Si quiero todo lo de la cocina, incluyendo cualquier cosa que pueda aparecer dentro de subniveles, usaría casa/cocina/#. Si solamente quiero los topics que están directamente dentro de casa/cocina, usaría casa/cocina/+.
import requests

respuesta = requests.get("https://httpbin.org/get")

print("Código de estado:", respuesta.status_code)
print("B5: la librería requests funciona dentro del contenedor.")
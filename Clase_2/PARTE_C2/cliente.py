import requests

url = "http://127.0.0.1:8000/libros"

session = requests.Session()

try:

    nuevo_libro = {
        "titulo": "El Hobbit",
        "paginas": 322,
        "editorial": {
            "nombre": "Minotauro",
            "pais": "España"
        }
    }

    respuesta_post = session.post(
        url,
        json=nuevo_libro,
        timeout=5
    )

    if respuesta_post.status_code in [200, 201]:
        print("ok")
    elif respuesta_post.status_code == 422:
        print("dato inválido")
    elif respuesta_post.status_code == 404:
        print("no existe")


    def listar_libros():
        respuesta_get = session.get(
            url,
            timeout=5
        )

        print("Libros:")
        print(respuesta_get.json())


    def reemplazar_libro(titulo):
        libro_nuevo = {
            "titulo": titulo,
            "paginas": 350,
            "editorial": {
                "nombre": "Minotauro",
                "pais": "España"
            },
            "disponible": True
        }

        respuesta_put = session.put(
            f"{url}/{titulo}",
            json=libro_nuevo,
            timeout=5
        )

        if respuesta_put.status_code == 200:
            print("Libro reemplazado correctamente")
        elif respuesta_put.status_code == 404:
            print("no existe")


    def borrar_libro(titulo):
        respuesta_delete = session.delete(
            f"{url}/{titulo}",
            timeout=5
        )

        if respuesta_delete.status_code == 204:
            print("Libro borrado correctamente")
        elif respuesta_delete.status_code == 404:
            print("no existe")


    listar_libros()

    reemplazar_libro("El Hobbit")

    listar_libros()

    borrar_libro("El Hobbit")

    listar_libros()


except requests.exceptions.Timeout:
    print("la solicitud tardó demasiado")

except requests.exceptions.ConnectionError:
    print("no se pudo conectar")

finally:
    session.close()
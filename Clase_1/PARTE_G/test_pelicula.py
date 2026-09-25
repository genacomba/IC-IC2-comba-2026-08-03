from funciones import obtener_dato

def test_clave_inexistente():
    pelicula = {
    "titulo": "Relatos salvajes",
    "anio": 2014,
    "director": "Damián Szifron"
}
    assert obtener_dato(pelicula, "duracion" ) == "desconocido"

from funciones import promedio

def test_promedio_lista_vacia():
    assert promedio([]) == "No hay notas"
from funciones import estadisticas

def test_estadisticas():
    resultado = estadisticas([7, 4, 9, 10, 6]) 
    assert resultado["promedio"] == 7.2
    assert resultado["maximo"] == 10
    assert resultado["minimo"] == 4
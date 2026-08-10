import pytest
from funciones import aprobo


@pytest.mark.parametrize(
    "notas, esperado",
    [
        ([6, 7, 8, 6], True),
        ([4, 2, 3, 7], False),
        ([4, 8, 3, 9], True),
    ]
)
def test_aprobo(notas, esperado):
    assert aprobo(notas) == esperado
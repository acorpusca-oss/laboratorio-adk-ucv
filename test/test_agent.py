from agente_ucv.agent import explicar_concepto, calcular_promedio
def test_calcular_promedio():
    notas = [10, 8, 9, 7]
    resultado = calcular_promedio(notas)
    assert resultado["status"] == "success"
    assert resultado["promedio"] == 8.5

def test_lista_vacia():
    resultado = calcular_promedio([])

    assert resultado["status"] == "error"


def test_nota_fuera_de_rango():
    resultado = calcular_promedio([15, 25, 18])

    assert resultado["status"] == "error"


def test_nota_con_texto():
    resultado = calcular_promedio([15, "hola", 18])

    assert resultado["status"] == "error"
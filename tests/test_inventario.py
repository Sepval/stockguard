import pytest

from src.inventario import (
    clasificar_stock,
    detectar_sobrestock,
    porcentaje_inventario,
)


# Pruebas de la regla principal de clasificación.
def test_stock_agotado():
    assert clasificar_stock(0, 20) == "AGOTADO"


def test_stock_critico():
    assert clasificar_stock(7, 20) == "CRITICO"


def test_stock_critico_en_el_limite_del_50_por_ciento():
    assert clasificar_stock(10, 20) == "CRITICO"


def test_stock_bajo():
    assert clasificar_stock(15, 20) == "BAJO"


def test_stock_bajo_en_el_limite_minimo():
    assert clasificar_stock(20, 20) == "BAJO"


def test_stock_normal():
    assert clasificar_stock(21, 20) == "NORMAL"


def test_stock_actual_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock actual"):
        clasificar_stock(-2, 20)


def test_stock_minimo_cero_es_invalido():
    with pytest.raises(ValueError, match="stock minimo"):
        clasificar_stock(5, 0)


def test_stock_minimo_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock minimo"):
        clasificar_stock(5, -1)


# Pruebas de la mejora propia: detección de sobrestock.
def test_sobrestock_detectado():
    assert detectar_sobrestock(120, 100) is True


def test_sobrestock_igual_al_maximo_no_se_detecta():
    assert detectar_sobrestock(100, 100) is False


def test_sobrestock_por_debajo_del_maximo_no_se_detecta():
    assert detectar_sobrestock(80, 100) is False


def test_sobrestock_stock_actual_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock actual"):
        detectar_sobrestock(-1, 100)


def test_sobrestock_maximo_cero_es_invalido():
    with pytest.raises(ValueError, match="stock maximo"):
        detectar_sobrestock(10, 0)


def test_sobrestock_maximo_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock maximo"):
        detectar_sobrestock(10, -5)


# Pruebas del cálculo del porcentaje de inventario.
def test_porcentaje_inventario_50_por_ciento():
    assert porcentaje_inventario(10, 20) == 50.0


def test_porcentaje_inventario_cero():
    assert porcentaje_inventario(0, 20) == 0.0


def test_porcentaje_inventario_100_por_ciento():
    assert porcentaje_inventario(20, 20) == 100.0


def test_porcentaje_inventario_puede_superar_el_100_por_ciento():
    assert porcentaje_inventario(30, 20) == 150.0


def test_porcentaje_inventario_redondea_a_dos_decimales():
    assert porcentaje_inventario(1, 3) == 33.33


def test_porcentaje_stock_actual_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock actual"):
        porcentaje_inventario(-1, 20)


def test_porcentaje_stock_minimo_cero_es_invalido():
    with pytest.raises(ValueError, match="stock minimo"):
        porcentaje_inventario(10, 0)


def test_porcentaje_stock_minimo_negativo_es_invalido():
    with pytest.raises(ValueError, match="stock minimo"):
        porcentaje_inventario(10, -5)

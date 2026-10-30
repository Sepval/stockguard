def clasificar_stock(stock_actual: int, stock_minimo: int) -> str:
    """Clasifica el nivel de riesgo según las unidades disponibles."""
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_minimo <= 0:
        raise ValueError("El stock minimo debe ser mayor que cero")

    if stock_actual == 0:
        return "AGOTADO"
    # Se evita usar 0.5 para mantener la comparación con cantidades enteras.
    if stock_actual * 2 <= stock_minimo:
        return "CRITICO"
    if stock_actual <= stock_minimo:
        return "BAJO"
    return "NORMAL"


def detectar_sobrestock(stock_actual: int, stock_maximo: int) -> bool:
    """Devuelve True si el inventario supera el máximo permitido."""
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_maximo <= 0:
        raise ValueError("El stock maximo debe ser mayor que cero")
    return stock_actual > stock_maximo


def porcentaje_inventario(stock_actual: int, stock_minimo: int) -> float:
    """Calcula el stock actual como porcentaje del stock mínimo."""
    if stock_actual < 0:
        raise ValueError("El stock actual no puede ser negativo")
    if stock_minimo <= 0:
        raise ValueError("El stock minimo debe ser mayor que cero")
    return round(stock_actual / stock_minimo * 100, 2)

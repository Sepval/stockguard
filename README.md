# StockGuard - Práctica de GitHub Actions

## 1. Objetivo

StockGuard es un ejemplo académico para practicar Integración Continua (CI) con Python, `pytest` y GitHub Actions. Clasifica el riesgo de inventario y contiene dos mejoras propias: detectar sobrestock y calcular el porcentaje de inventario con respecto al stock mínimo.

> Este repositorio es un caso de práctica. No es la solución de negocio del proyecto final RapidGo 360.

## 2. Reglas de negocio

### Clasificación del inventario

| Condición | Resultado |
|---|---|
| Stock actual igual a cero | `AGOTADO` |
| Stock actual mayor que cero y menor o igual al 50 % del stock mínimo | `CRITICO` |
| Stock actual mayor al 50 % y menor o igual al stock mínimo | `BAJO` |
| Stock actual mayor al stock mínimo | `NORMAL` |
| Stock actual negativo o stock mínimo menor o igual a cero | Error `ValueError` |

### Mejoras propias

- `detectar_sobrestock(stock_actual, stock_maximo)`: devuelve `True` cuando el stock supera estrictamente el máximo. Si es igual al máximo, devuelve `False`.
- `porcentaje_inventario(stock_actual, stock_minimo)`: devuelve el stock actual como porcentaje del mínimo, redondeado a dos decimales.

## 3. Estructura

```text
github-actions-stockguard/
├── .github/workflows/ci.yml
├── src/
│   ├── __init__.py
│   └── inventario.py
├── tests/
│   └── test_inventario.py
├── requirements.txt
├── pytest.ini
└── README.md
```

## 4. Ejecutar en Windows

Se requiere Python 3.12 o una versión compatible y Git.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m compileall src tests
python -m pytest -v
```

Si `py -3.12` no está disponible, revisa qué versiones de Python tienes instaladas y usa la que corresponda; para reproducir el workflow, se recomienda Python 3.12.

## 5. Qué verifica GitHub Actions

El archivo `.github/workflows/ci.yml` se ejecuta en estos casos:

- `push` a `main`.
- Pull Request cuya rama destino sea `main`.
- Inicio manual desde la pestaña **Actions** mediante `workflow_dispatch`.

El job `validar-python` utiliza un runner Linux limpio y realiza estos pasos: descarga el repositorio, configura Python 3.12, instala las dependencias declaradas, comprueba la sintaxis Python y ejecuta las pruebas unitarias.

Un resultado verde solo indica que estas comprobaciones pasaron; no demuestra que una infraestructura completa de Kafka, Spark, Airflow o Docker funcione.

## 6. Cómo practicar un fallo controlado

1. Cambia temporalmente en `tests/test_inventario.py` la expectativa de `test_stock_critico` de `"CRITICO"` a `"NORMAL"`.
2. Ejecuta `python -m pytest -v` y observa que falla esa prueba, porque 7 unidades con un mínimo de 20 corresponden a `CRITICO`.
3. Para reproducir el escenario en GitHub, haz el cambio en un repositorio de práctica, envíalo y revisa el step **Ejecutar pruebas** en Actions.
4. Restaura el resultado esperado `"CRITICO"`, vuelve a ejecutar las pruebas y confirma que pasan.

No introduzcas un fallo intencional en la rama principal de un proyecto compartido. Para RapidGo 360, haz esta práctica únicamente en el repositorio de ejemplo o en una rama temporal.

## 7. Mejora mediante Pull Request

Crea una rama para un cambio real, añade al menos dos pruebas que lo verifiquen, envíala a GitHub y abre un Pull Request hacia `main`. Espera los checks y revisa sus logs antes de hacer merge. Para impedir técnicamente un merge con checks fallidos, configura en GitHub una regla de protección de rama que exija el check correspondiente; definir el workflow por sí solo no activa esa protección.

## 8. Evidencias para la actividad

Conserva capturas o enlaces de:

1. Una ejecución exitosa que muestre workflow, job y steps.
2. La ejecución fallida por el error intencional.
3. La ejecución posterior corregida.
4. Un Pull Request con los checks de Actions.
5. Una ejecución manual mediante `workflow_dispatch`.
6. El commit o Pull Request que incorpore la mejora y sus pruebas.

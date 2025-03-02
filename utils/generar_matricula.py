import datetime
import random


def generar_matricula(prefix="UAO", longitud_id=4) -> str:
    """
    Genera un número de matrícula escolar.

    Parámetros:
    - prefix: Prefijo de la universidad.
    - longitud_id: Número de dígitos para el identificador único.

    Retorna:
    - str: Matrícula generada.
    """
    year = str(datetime.datetime.now().year)[
        -2:
    ]  # Obtiene los últimos 2 dígitos del año actual
    identificador = random.randint(
        10 ** (longitud_id - 1), 10**longitud_id - 1
    )  # Genera ID aleatorio
    return f"{year}{prefix}{identificador}"

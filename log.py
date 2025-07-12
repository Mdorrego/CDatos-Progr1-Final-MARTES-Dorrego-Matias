import logging
import os

""" Configuro la función para llevar registro de libros guardados y eliminados. """
def configurar_registros():
    os.makedirs("logs", exist_ok=True)

    logging.basicConfig(
        filename="logs/registros.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"
    )
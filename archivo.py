import json
import os
import logging

RUTA_ARCHIVO = "data/libros.json"

""" Cargo la lista de libros desde un archivo JSON. Si el archivo no existe o está vacío, retorna una lista vacía. """
def cargar_datos():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    try:
        with open(RUTA_ARCHIVO, "r") as f:
            datos = json.load(f)
            if isinstance(datos, list):
                return datos
            else:
                print("⚠️ El archivo no contiene una lista válida.")
                return []
    except json.JSONDecodeError:
        logging.error(f"❌ Error de lectura JSON: {e}")
        return []
    except Exception as e:
        print(f"❌ Error inesperado al cargar datos: {e}")
        return []

""" Guardo la lista de libros en un archivo JSON. """
def guardar_datos(lista):
    try:
        os.makedirs(os.path.dirname(RUTA_ARCHIVO), exist_ok=True)
        with open(RUTA_ARCHIVO, "w") as f:
            json.dump(lista, f, indent=4, ensure_ascii=False)
        print("💾 Datos guardados correctamente.")
    except Exception as e:
        print(f"❌ Error al guardar los datos: {e}")
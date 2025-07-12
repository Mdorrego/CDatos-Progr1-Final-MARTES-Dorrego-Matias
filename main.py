import questionary
import logging
from libros import agregar_libro, listar_libros, buscar_libros, eliminar_libro
from archivo import cargar_datos, guardar_datos
from log import configurar_registros
configurar_registros()

""" Función principal. Contiene el menú con questionary por el cual navego el programa. """
def main():
    libros = cargar_datos()
    while True:
        opcion = questionary.select(
            "📚 Seleccioná una opción:",
            choices=[
                "1. Agregar libro",
                "2. Listar todos los libros",
                "3. Buscar libros",
                "4. Eliminar libro",
                "5. Salir"
            ]
        ).ask()

        if opcion.startswith("1"):
            nuevo = agregar_libro()
            libros.append(nuevo)
        elif opcion.startswith("2"):
            listar_libros(libros)
        elif opcion.startswith("3"):
            buscar_libros(libros)
        elif opcion.startswith("4"):
            eliminar_libro(libros)
        elif opcion.startswith("5"):
            guardar_datos(libros)
            print("✅ Datos guardados. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main()
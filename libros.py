import questionary
import logging
from utils import es_entero, es_isbn_valido

""" Solicito al usuario los datos del libro y devuelvo un diccionario con la información. Valida que los campos no estén vacíos y que el año sea un número. """
def agregar_libro():
    titulo = questionary.text("Título del libro:").ask()
    while not titulo.strip():
        print("❌ El título no puede estar vacío.")
        titulo = questionary.text("Título del libro:").ask()

    autor = questionary.text("Autor del libro:").ask()
    while not autor.strip():
        print("❌ El autor no puede estar vacío.")
        autor = questionary.text("Autor del libro:").ask()
    genero = questionary.text("Género:").ask()

    año = questionary.text("Año de publicación:").ask()
    while not es_entero(año):
        print("❌ Año inválido. Ingresá un número.")
        año = questionary.text("Año de publicación:").ask()

    isbn = questionary.text("ISBN (opcional):").ask()
    if isbn and not es_isbn_valido(isbn):
        print("⚠️ ISBN no válido. Se dejará vacío.")
        isbn = ""

    libro = {
        "titulo": titulo.strip(),
        "autor": autor.strip(),
        "genero": genero.strip(),
        "año": int(año),
        "isbn": isbn.strip()
    }

    """ Registro el libro guardado """
    logging.info(f"Libro agregado: {libro['titulo']} por {libro['autor']}")
    return libro

""" Muestra todos los libros en la lista, uno por uno con formato. Si la lista está vacía, informa al usuario. """
def listar_libros(lista):
    if not lista:
        print("No hay libros cargados.")
        return

    print("\n📚 LISTA DE LIBROS 📚")
    for idx, libro in enumerate(lista, 1):
        print(f"\n📖 Libro {idx}")
        print(f"   Título : {libro['titulo']}")
        print(f"   Autor  : {libro['autor']}")
        print(f"   Género : {libro['genero']}")
        print(f"   Año    : {libro['año']}")
        print(f"   ISBN   : {libro['isbn'] if libro['isbn'] else 'No especificado'}")

""" Permite buscar libros por título, autor o género. Muestra todos los resultados encontrados. """
def buscar_libros(lista):
    if not lista:
        print("No hay libros cargados para buscar.")
        return

    criterio = questionary.select(
        "¿Por qué campo querés buscar?",
        choices=["Titulo", "Autor", "Genero"]
    ).ask()

    termino = questionary.text(f"Ingresá el {criterio.lower()} a buscar:").ask().strip().lower()

    resultados = [
        libro for libro in lista
        if termino in libro[criterio.lower()].lower()
    ]

    if resultados:
        print(f"\n🔎 Se encontraron {len(resultados)} resultado(s):")
        for idx, libro in enumerate(resultados, 1):
            print(f"\n📖 Libro {idx}")
            print(f"   Título : {libro['titulo']}")
            print(f"   Autor  : {libro['autor']}")
            print(f"   Género : {libro['genero']}")
            print(f"   Año    : {libro['año']}")
            print(f"   ISBN   : {libro['isbn'] if libro['isbn'] else 'No especificado'}")
    else:
        print("❌ No se encontraron coincidencias.")

"""  Permite eliminar un libro por Título o ISBN. Si hay múltiples libros, los muestra para elegir. """
def eliminar_libro(lista):
    if not lista:
        print("No hay libros para eliminar.")
        return

    metodo = questionary.select(
        "¿Cómo querés buscar el libro a eliminar?",
        choices=["Por título", "Por ISBN"]
    ).ask()

    campo = "titulo" if metodo == "Por título" else "isbn"
    termino = questionary.text(f"Ingresá el {campo} del libro:").ask().strip().lower()

    coincidencias = [
        (i, libro) for i, libro in enumerate(lista)
        if termino in libro[campo].lower()
    ]

    if not coincidencias:
        print("❌ No se encontraron libros que coincidan.")
        return

    if len(coincidencias) == 1:
        idx, libro = coincidencias[0]
    else:
        opciones = [
            f"{i}. {libro['titulo']} - {libro['autor']}" for i, libro in coincidencias
        ]
        seleccion = questionary.select(
            "Seleccioná el libro que querés eliminar:",
            choices=opciones
        ).ask()
        idx = int(seleccion.split(".")[0])  

    libro_eliminado = lista.pop(idx)
    """ Registro el libro eliminado """
    logging.info(f"Libro eliminado: {libro_eliminado['titulo']} por {libro_eliminado['autor']}")  
    print(f"✅ Libro eliminado: {libro_eliminado['titulo']} - {libro_eliminado['autor']}")
""" Verifico si el valor ingresado es entero """
def es_entero(valor):                                   
    try:
        int(valor)
        return True
    except ValueError:
        return False

""" Valido el formato del código ISBN """
def es_isbn_valido(isbn):                               
    return isbn.isdigit() and len(isbn) in [10, 13]

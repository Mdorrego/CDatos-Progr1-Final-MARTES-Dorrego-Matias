# Sistema de Biblioteca en Python

Este proyecto consiste en un sistema de biblioteca por consola, desarrollado como trabajo final para la materia Programación 1 en la carrera de Ciencia de Datos ISTEA 2025 1C a cargo del profesor Juan Pablo Sosa.

Permite gestionar libros agregándolos, listándolos, buscándolos y eliminándolos con la librería para interfaz gráfica `questionary`.

---

## Tecnologías utilizadas

- Python 3.11+
- Librería externa: [`questionary`]
- Formato de datos: JSON
- Buenas prácticas: PEP8, PEP257, Zen of Python
- Entorno virtual: `venv`

---

## Funcionalidades

- Agregar libro
- Listar todos los libros
- Buscar por título, autor o género
- Eliminar libro por título o ISBN
- Guardado automático en archivo JSON

<img width="1140" height="231" alt="image" src="https://github.com/user-attachments/assets/1f294e17-f3df-4d4f-b0dc-da7779d89a55" />

---

## Instalación y uso
### 1. Clonar el repositorio

```bash
git clone https://github.com/Mdorrego/CDatos-Progr1-Final-MARTES-Dorrego-Matias.git
cd CDatos-Progr1-Final-MARTES-Dorrego-Matias
```

### 2. Manejo del entorno virtual

- Crear el entorno virtual
python -m venv venv

- Activar el entorno virtual
venv\Scripts\activate (WINDOWS)
source venv/bin/activate (MAC/LINUX)

- Instalar dependencias
pip install -r requirements.txt

- Ejecutar el programa
python main.py

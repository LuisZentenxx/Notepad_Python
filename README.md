# Bloc de Notas en PyQt5

Este es un simple proyecto de un Bloc de Notas desarrollado en Python utilizando la biblioteca PyQt5. El Bloc de Notas permite crear, abrir, guardar, cambiar el color de fondo, cambiar el color de fuente y cerrar pestañas.

## Características

- Crear nuevas pestañas.
- Abrir archivos de texto existentes.
- Guardar el contenido en archivos de texto.
- Cambiar el color de fuente.
- Cambiar el color de fondo de la pestaña de edición.

## Requisitos

- Python 3.x
- PyQt5

## Uso

1. Clona el repositorio o descarga los archivos.

2. Instala PyQt5 si no lo tienes instalado:

   ```bash
   pip install PyQt5

3. Ejecución de la aplicación
    ```bash
   python notepad.py

## Personalización

1. Puedes personalizar la fuente predeterminada y otros aspectos de la aplicación editando el código en **notepad.py**.

    ```bash
    def new_tab(self):

    text_edit = QTextEdit()
    font = QFont("Arial", 12)  
    text_edit.setFont(font)
    self.tabs.addTab(text_edit, "Nueva Pestaña")
   

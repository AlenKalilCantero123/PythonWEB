# TuPrimeraPaginaCantero

# Blog Project

Este es un proyecto Django que implementa una plataforma de blog, donde los usuarios pueden crear autores, categorías y publicaciones. La aplicación permite crear, editar y buscar publicaciones, así como gestionar autores y categorías.

## Funcionalidades

El proyecto tiene las siguientes funcionalidades:

1. **Página de inicio**: Muestra la bienvenida al usuario.
2. **Creación de autores**: Permite crear nuevos autores para asociarlos a las publicaciones.
3. **Creación de categorías**: Permite crear nuevas categorías para organizar las publicaciones.
4. **Creación de publicaciones**: Permite crear publicaciones que se pueden asociar con un autor y una categoría.
5. **Búsqueda de publicaciones**: Permite buscar publicaciones por título.

## Estructura del Proyecto

### Vistas:

1. **Página de inicio (`/`)**:
   - Ruta: `http://127.0.0.1:8000/`
   - Muestra un mensaje simple de bienvenida: "Hello, World!".

2. **Página para crear autores (`/create_author/`)**:
   - Ruta: `http://127.0.0.1:8000/create_author/`
   - Funcionalidad: Formulario para crear un nuevo autor.

3. **Página para crear categorías (`/create_category/`)**:
   - Ruta: `http://127.0.0.1:8000/create_category/`
   - Funcionalidad: Formulario para crear una nueva categoría.

4. **Página para crear publicaciones (`/create_post/`)**:
   - Ruta: `http://127.0.0.1:8000/create_post/`
   - Funcionalidad: Formulario para crear una nueva publicación.

5. **Página de búsqueda de publicaciones (`/search/`)**:
   - Ruta: `http://127.0.0.1:8000/search/`
   - Funcionalidad: Permite buscar publicaciones por título.

## Instrucciones para probar las funcionalidades

1. **Configura el entorno de desarrollo**:
   - Asegúrate de tener Python y Django instalados.
   - Instala las dependencias necesarias:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecuta el servidor de desarrollo**:
   - Para iniciar el servidor de desarrollo de Django, ejecuta:
     ```bash
     python manage.py runserver
     ```

3. **Probar las funcionalidades en orden**:

   1. **Página de inicio**:
      - Abre el navegador y navega a `http://127.0.0.1:8000/`.
      - Deberías ver el mensaje "Hello, World!".

   2. **Crear un autor**:
      - Navega a `http://127.0.0.1:8000/create_author/`.
      - Completa el formulario para crear un nuevo autor y guarda el autor.
      - Después de guardar, serás redirigido a la página de inicio.

   3. **Crear una categoría**:
      - Navega a `http://127.0.0.1:8000/create_category/`.
      - Completa el formulario para crear una nueva categoría y guarda la categoría.
      - Serás redirigido a la página de inicio después de guardar.

   4. **Crear una publicación**:
      - Navega a `http://127.0.0.1:8000/create_post/`.
      - Completa el formulario para crear una nueva publicación.
      - En el formulario de creación de publicaciones, selecciona un autor y una categoría previamente creados.
      - Después de guardar la publicación, serás redirigido a la página de inicio.

   5. **Buscar publicaciones**:
      - Navega a `http://127.0.0.1:8000/search/`.
      - Introduce un término de búsqueda en el campo de búsqueda (por ejemplo, el título de una publicación) y haz clic en el botón de búsqueda.
      - Verás los resultados de las publicaciones que coinciden con el término de búsqueda.

## Archivos importantes

1. **`views.py`**: Contiene la lógica para manejar las vistas.
2. **`models.py`**: Define los modelos de datos (Autor, Categoría, Publicación).
3. **`forms.py`**: Contiene los formularios para la creación de autores, categorías y publicaciones.
4. **`templates/`**: Carpeta que contiene los archivos HTML para las plantillas.
   - **`base.html`**: Plantilla base para la aplicación.
   - **`create_author.html`**: Plantilla para la creación de autores.
   - **`create_category.html`**: Plantilla para la creación de categorías.
   - **`create_post.html`**: Plantilla para la creación de publicaciones.
   - **`search.html`**: Plantilla para la búsqueda de publicaciones.

## Requerimientos

- Python 3.13+
- Django 5.1.4

Puedes agregar más detalles específicos, como instrucciones sobre cómo configurar el entorno virtual, base de datos, o instalar dependencias, si lo necesitas.

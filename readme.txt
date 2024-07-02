=== Proyecto de Tienda de Zapatillas ===

Este proyecto de Django es una tienda en línea para la venta de zapatillas.

### Instalación ###

Para comenzar, asegúrate de tener Python y pip instalados en tu sistema.

1. Instala Django 4.2 y Pillow utilizando pip:

pip install django==4.2
pip install Pillow


### Configuración ###

1. Clona este repositorio o descarga los archivos del proyecto.

2. Navega a la carpeta del proyecto:

cd nombre_de_tu_carpeta


3. Realiza las migraciones de la base de datos:

python manage.py migrate


4. Crea un superusuario para acceder al panel de administración:

python manage.py createsuperuser


5. Inicia el servidor de desarrollo:

python manage.py runserver



6. Abre tu navegador y visita `http://127.0.0.1:8000/` para ver la aplicación en acción.

### Estructura del Proyecto ###

- `manage.py`: Archivo de gestión de Django para ejecutar comandos de administración.
- `nombre_de_tu_proyecto/`: Carpeta principal del proyecto Django.
- `nombre_de_tu_app/`: Carpeta de la aplicación específica para la tienda de zapatillas.
- Otros archivos y carpetas: Dependiendo de tu estructura de proyecto personalizada.

### Notas Adicionales ###

- Asegúrate de configurar adecuadamente tu entorno virtual o entorno de desarrollo según tus necesidades específicas.
-


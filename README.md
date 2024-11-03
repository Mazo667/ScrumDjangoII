# ACTIVIDAD GRUPAL DE DJANGO SOBRE SCRUM II

El objetivo de este trabajo práctico es implementar un sistema básico de gestión de usuarios
en Django, que permita a los estudiantes comprender y aplicar conceptos de autenticación,
autorización, administración de sesiones, inicio y cierre de sesión, así como el uso de
permisos y grupos de usuarios.

## Integrantes
   - Emilia Alvarez
   - Marcela Delgado
   - Maximiliano Fava
   - Jessica Loureiro

## Instalación

1. Crea un entorno virtual (opcional pero recomendado):
    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa `env\Scripts\activate`
    ```

2. Clona el repositorio:

   ```bash
   git clone https://github.com/Mazo667/ScrumDjango.git
   cd ScrumDjango
    ```

3. Instala los paquetes requeridos:
    ```bash
    pip install -r requirements.txt
    ```

4. Poblamos la base de datos:
   ```bash
    python poblar_db.py
    ```

5. Ejecutamos el servidor
   ```bash
    python manage.py runserver
    ```

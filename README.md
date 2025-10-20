# Proyecto Web

## Cómo ejecutar (Windows)
1. Clonar o descargar y extraer el ZIP.
2. Crear y activar un entorno virtual:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Instalar dependencias:
   ```
   pip install -r requirements.txt
   ```
4. Migrar la base de datos y crear superusuario (opcional):
   ```
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Ejecutar servidor:
   ```
   python manage.py runserver
   ```
6. Probar funcionalidades (orden recomendado):
   - Ir a `http://127.0.0.1:8000/` → Inicio.
   - `http://127.0.0.1:8000/persona/` → Crear Persona.
   - `http://127.0.0.1:8000/producto/` → Crear Producto.
   - `http://127.0.0.1:8000/orden/` → Crear Orden (elige Persona y Producto).
   - `http://127.0.0.1:8000/buscar/` → Buscar por nombre (Persona/Producto).

## Estructura principal
- django_web/       -> configuración del proyecto
- app_main/         -> app con models, views, forms, templates
- requirements.txt
- README.md

## Notas
- Código comentado en español.
- Base de datos por defecto: SQLite (`db.sqlite3` en la raíz del proyecto).

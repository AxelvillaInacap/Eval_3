# (EVAL_3) Gestión de Asistencias Técnicas para PYMEs

Este proyecto corresponde a la **Evaluación 3** de la asignatura **Programación Backend**.  
Consiste en una aplicación web interna desarrollada en **Django**, destinada a gestionar asistencias técnicas para PYMEs locales.  
Permite administrar solicitudes, servicios, profesionales asignados y empresas clientes.

---

## 👥 Integrantes del Equipo

- **Axel Vilela Poblete**  
  *Módulos:* `Empresa`, `OrdenServicio`, estructura base y autenticación.

- **Juan Herrera**  
  *Módulo:* `Servicio`.

- **Sebastian Ovando**  
  *Módulo:* `Profesional`.

---

## ✨ Características Principales

La aplicación cumple con todos los requisitos funcionales evaluados:

### ✅ CRUD Completo
Gestión total (Crear, Leer, Actualizar y Eliminar) de las 4 entidades:
- Empresas  
- Servicios  
- Profesionales  
- Órdenes de Servicio  

### ✅ Modelo Relacional
- `OrdenServicio` se relaciona con:
  - `Empresa` (ForeignKey)  
  - `Profesional` (ForeignKey)  
  - `Servicio` (ManyToManyField)

### ✅ Administración Avanzada
El panel `/admin` incluye:
- `list_display`  
- `list_filter`  
- `search_fields`  

### ✅ Búsquedas y Filtros
Cada módulo público posee su propia barra de búsqueda funcional.

### ✅ Autenticación
- Todas las acciones que modifican datos (Crear, Editar, Eliminar) requieren inicio de sesión.
- Las vistas de lista y detalle son públicas.

### ✅ Interfaz con Bootstrap
- Plantilla base (`base.html`)
- Bootstrap 5 (vía CDN)
- Navbar responsiva y diseño limpio

---

## 🛠️ Stack Tecnológico

- **Backend:** Python 3.11+  
- **Framework:** Django 5.x  
- **Base de Datos:** SQLite 3  
- **Frontend:** HTML5 + Bootstrap 5

---

## 🚀 Ejecución Local

Sigue estos pasos para levantar el proyecto:

```bash
git clone [https://github.com/AxelvillaInacap/Eval_3]
cd Eval_3

# Crear entorno virtual
python -m venv venv

# Activar entorno (Windows)
.\venv\Scripts\activate

# Activar entorno (macOS/Linux)
# source venv/bin/activate

# Instalar Django
pip install django

# Entrar a la carpeta del proyecto
cd AsissTecnicasPymes

# Aplicar migraciones
python manage.py migrate

# Crear superusuario
python manage.py createsuperuser

# Ejecutar servidor
python manage.py runserver
´´´
-----------------------------------

## 🧪 Cómo Probar la Aplicación

1. **Acceder al módulo principal:**  
   Visita: `http://127.0.0.1:8000/pymes/ordenes/`

2. **Comprobar la seguridad sin iniciar sesión:**  
   - Intenta crear una nueva orden.  
   - O intenta usar los botones **Editar** o **Eliminar** en cualquier vista.  
   - Debes ser redirigido automáticamente a la página de **Login**: `/login/`.

3. **Iniciar sesión:**  
   - Ingresa con el superusuario creado durante la instalación.  
   - Tras iniciar sesión, volverás a la lista de órdenes.  
   - En el navbar deberá aparecer: **"Hola, <tu_usuario>"**.

4. **Crear datos iniciales (necesario para que funcione el flujo):**  
   Entra a: `http://127.0.0.1:8000/admin/`  
   Y crea al menos:
   - 1 **Empresa**  
   - 1 **Servicio**  
   - 1 **Profesional**

5. **Probar el flujo completo de una Orden de Servicio:**  
   - En `.../pymes/ordenes/`, haz clic en **"Crear Nueva Orden"**.  
   - Completa el formulario (los select y checkboxes mostrarán los datos creados en el admin).  
   - Guarda la orden.  
   - Prueba los botones:
     - **Ver**
     - **Editar**
     - **Eliminar**

6. **Cerrar sesión:**  
   - Haz clic en **"Cerrar Sesión"** en el navbar.  
   - Serás deslogueado y redirigido a la página principal.  
   - El navbar volverá a mostrar **"Iniciar Sesión"**.

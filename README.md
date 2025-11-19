# (EVAL_3) Gestión de Asistencias Técnicas PYMES

Este proyecto es la Evaluación 3 para la asignatura de Programación Backend. Es una aplicación web interna desarrollada en Django para gestionar asistencias técnicas a PYMEs locales, cubriendo la gestión de solicitudes, servicios, profesionales asignados y las empresas clientes.

## 👥 Integrantes del Equipo
* **Axel Vilela Poblete** (Módulos: `Empresa`, `OrdenServicio`, Estructura Base, Autenticación y UI)
* **Juan Herrera** (Módulo: `Servicio`)
* **Sebastian Ovando** (Módulo: `Profesional`)

---

## ✨ Características Principales
La aplicación cumple con todos los requisitos funcionales y añade mejoras de experiencia de usuario (UX):

* **CRUD Completo:** Gestión total (Crear, Leer, Actualizar, Eliminar) para las 4 entidades: Empresas, Servicios, Profesionales y Órdenes de Servicio.
* **Modelo Relacional:** Conexión robusta entre entidades mediante `ForeignKey` y `ManyToManyField`.
* **Admin Avanzado:** Panel de administración personalizado con filtros, búsqueda y columnas específicas.
* **Búsqueda Pública:** Barras de búsqueda funcionales en todos los listados principales.
* **Seguridad:** Protección de vistas críticas con `@login_required` y sistema completo de Login/Logout.
* **Interfaz Moderna (UI/UX):**
    * **Tema Profesional:** Estilizado con Bootstrap 5 (Tema "Litera").
    * **Modo Oscuro:** Interruptor integrado para cambiar entre tema Claro/Oscuro con detección automática del sistema.
    * **Internacionalización (i18n):** Soporte configurado para cambio de idioma (Español/Inglés).
    * **Dashboard:** Tablero de control principal con estadísticas y métricas en tiempo real.

## 🛠️ Stack Tecnológico
* **Backend:** Python 3.11+
* **Framework:** Django 5.x
* **Base de Datos:** SQLite 3
* **Frontend:** HTML5, Bootstrap 5 (Bootswatch), Bootstrap Icons, JavaScript

---

## 🚀 Instrucciones de Ejecución Local

Sigue estos pasos para levantar el proyecto en tu máquina:

### 1. Clonar el Repositorio
```bash
git clone [https://github.com/AxelvillaInacap/Eval_3](https://github.com/AxelvillaInacap/Eval_3)
cd Eval_3
```
### 2. Crear y Activar Entorno Virtual
```bash
# Crear el venv (si no existe)
python -m venv venv

# Activar en Windows (PowerShell/CMD)
.\venv\Scripts\activate

# Activar en macOS/Linux
# source venv/bin/activate
```
### 3. Instalar Dependencias
```bash
pip intall django
```
### 4. Preparar la Base de Datos
```bash
cd AsissTecnicasPymes
python manage.py migrate
```
### 5. Crear un SuperUsuario
```bash
python manage.py createsuperuser
```
### 6. Ejecuta el Servidor
```bash
python manage.py runserver
```

### 🚀🚀🚀 !El servidor estará corriendo en http://127.0.0.1:8000/! 🚀🚀🚀



## 🧪 Cómo Probar la Aplicación

1. **Login y Dashboard:**
    * Al intentar entrar a cualquier función de crear/editar, serás redirigido al Login.
    * Ingresa con tu superusuario. Serás recibido por el **Dashboard de Estadísticas**.

2. **Probar UI:**
    * Haz clic en el icono de **Luna/Sol** en la barra superior para probar el Modo Oscuro.
    * Haz clic en el icono del **Mundo** para probar el selector de idioma.

3. **Flujo de Trabajo:**
    * Navega a "Empresas", "Servicios" o "Profesionales" para crear los datos base.
    * Ve a "Órdenes" y crea una nueva Orden de Servicio, conectando todos los datos anteriores.

4. **Gestión:**
    * Utiliza los botones de acción (Ojo, Lápiz, Basura) en las tablas para Ver, Editar o Eliminar registros.



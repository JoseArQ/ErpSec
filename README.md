## Prerrequisitos

Antes de comenzar, asegúrate de tener instalados los siguientes componentes en tu sistema:

- Python 3.8 o superior
- Pip (administrador de paquetes de Python)
- PostgreSQL: Se requiere tener creada una base de datos con el nombre de *erp*

## Paso 1: Clonar el Repositorio

Clona el repositorio de tu proyecto Django desde tu sistema de control de versiones (por ejemplo, GitHub, GitLab).

```bash
git clone https://github.com/JoseArQ/ErpSec.git
cd ErpSec
```

## Paso 2
### Crear un entorno virtual
```bash
python -m venv venv
```

### Activar el entorno virtual (Windows)
```bash
.\venv\Scripts\activate
```

### Activar el entorno virtual (Linux/Mac)
```bash
source env/bin/activate
```

## Paso 3 Instalar dependencias
```bash
pip install -r requirements.txt
```

## Paso 4 Configurar archivo .env

```DEBUG=True
DB_NAME=db_name
DB_USER=db_user
DB_PASSWORD=db_password
DB_HOST=db_host
```

## Paso 5 Ejecutar Migraciones

```bash
python manage.py migrate
```

## Paso 6 Crear superuser

```bash
python manage.py createsuperuser
```

## Paso 7 Ejecutar Servidor

```bash 
python manage.py runserver
```
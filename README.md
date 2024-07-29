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

# Desarrollo Prueba Técnica

Para el desarrollo de la prueba se tomaran tres entidades User, Permission y Group, la idea es extender el sistema de permisos y roles que ya trae Django por defecto, ya que resuelve muy bien la gestion de usuarios por permisos y grupos de permisos, evitando así duplicar código innecesariamente.

Para resolver el problema se tienen en cuenta las siguientes relaciones: 

## User

- Un usuario puede tener uno o varios permisos. 
- Un usuario puede tener uno o varios grupos(roles)

## Permission

- Un permiso se le puede asignar a uno o más usuarios.
- Un permiso se le puede asiganr a uno o más grupos(roles). 

## Group

- Un grupo puede tener uno o más permisos.
- Un grupo puede estar asignado a un usuario o más 

Las relaciones previas argumentan una relación de muchos a muchos entre User y Permission, al igual que entre User y Group y entre Group y Permission. Esta configuración de relaciones permite que a un usuario se le puede asignar permisos de dos formas sin que sean excluyentes.
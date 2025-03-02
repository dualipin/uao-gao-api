# GradePay



## Diagrama de Entidad-Relación

```mermaid
erDiagram
    Persona {
        string nombre
        string apellido_paterno
        string apellido_materno
        date fecha_nacimiento
        string sexo
        string correo
        string telefono
        boolean activo
    }

    Estudiante {
        int id PK
        Persona p FK
        Carrera c FK
        string matricula UK
        string domicilio
    }

    Docente {
        int id PK
        string rfc UK
        Persona p FK
    }

    Carrera {
        int id PK
        string clave
        string nombre
    }

    Materia {
        int id PK
        string clave
        string nombre
        int semestre
        int creditos
        Carrera c FK
    }

    MateriaCalificacion {
        int id PK
        float calificacion
        Estudiante e FK
        Materia m FK
        Docente d FK
    }

```
```
GradePay-back
├─ app
│  ├─ calificaciones
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ carreras
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ docentes
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ estudiantes
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ materias
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  ├─ pagos
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  └─ __init__.py
│  │  ├─ models.py
│  │  ├─ tests.py
│  │  ├─ views.py
│  │  └─ __init__.py
│  └─ __init__.py
├─ config
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ README.md
├─ requirements.txt
└─ shared
   └─ models
      ├─ persona.py
      └─ __init__.py

```
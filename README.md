# DACS TPI
## Django Project

Trabajo Práctico Integrador - Desarrollo de Aplicaciones Cliente-Servidor (UTN - FRRe)

Integrantes:
  - Andrik, Ivan Danel.
  - Britos, Miguel Antonio.
  - Montero Cura, Facundo Farid.
  - Soto, Horacio Oscar.
  - Villegas, Cesar Manuel.

### Frameworks y liberías

A continuación se encuentra el listado de tecnologías a utilizar:

* [Django 3.0](https://www.djangoproject.com/) - a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Django REST framework 3.11](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.

### Instalación

1. Clonar este repositorio
```
git clone https://github.com/HoracioSoto/tpi.git
```

2. Ir a la carpeta e instalar el entorno virtual
```
virtualeenv env
```

3. Activar el entorno virtual

_Linux_:
```
source env/bin/activate
```
_Windows_:
```
./env/Scripts/activate
```

4. Instalar las dependencias
```
(env) pip install -r requirements.txt
```

5. Correr las migraciones
```
(env) python manage.py migrate
```

6. Levantar el servicio de Django
```
(env) python manage.py runserver 127.0.0.1:8000
```

License
----

GNU General Public License v3.0

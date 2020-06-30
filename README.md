# UP Chat
Aplicación web hecha en python con Flask y PostgreSQL.

## Requerimientos
- python (v3.6.8*)
- virtualenv (v20.0.20*)

\* Es posible que funcione con otras versiones, las listadas son las usadas en desarrollo.

## Estructura de Base de Datos
**Tablas:**
- **users**
    - **username** (varchar(150)) (PK)
    - **password** (varchar(100))
- **chats**
    - **id** (int) (PK auto incremental)
    - **user1** (varchar(150)) (FK)
    - **user2** (varchar(150)) (FK)
- **messages**
    - **id** (int) (PK auto incremental)
    - **chat** (int) (FK)
    - **from_user** (varchar(150)) (FK)
    - **date** (timestamp)
    - **message** (varchar(500))

## Configuración
- Crear en la base del proyecto un archivo .env copiando el .env.example y llenar campos con configuración 
deseada.
```
# Profiles: development, testing, production, default
PROFILE=development
SECRET_KEY=secretKey
DEV_DATABASE_URI=postgres://yourPostgreSQLDataBaseURI
TEST_DATABASE_URI=postgres://yourPostgreSQLDataBaseURI
PRODUCTION_DATABASE_URI=postgres://yourPostgreSQLDataBaseURI
```
- Para instalar las dependendencias del proyecto primero asegurarse de estar en un virtualenv activado, 
luego correr lo siguiente estando parado en la base del proyecto:
```
$ pip install --user -e .
# O sin el --user en caso de error
$ pip install -e .
```

## Desarrollo
- Para levantar la aplicacion en desarrollo primero hay que settear las siguientes variables de entorno por 
linea de comando:
```
$ export FLASK_APP=run.py
$ export FLASK_DEBUG=1
```
- Luego levantar la app con:
```
$ flask run
```
- Acceder por http://localhost:5000/

## Tests
Si se intenta correr todos los test al mismo tiempo puede tirar un error al superar el máximo de pool de conexiones. 
Se recomienda correr los test por separado al igual que correr su cobertura. Para poder generar un html de cobertura 
más completo se recomienda correr el "test_chat.py".
- Para correr los tests unitarios primero hay que settear la URI de la base de datos que vamos a usar por 
linea de comando:
```
$ export TEST_DATABASE_URI=postgres://yourPostgreSQLDataBaseURI
```
- Luego correr los tests:
```
$ python -m unittest
```
- Para correr un test en especifico correr:
```
$ python test_nombre.py
```
- Para correr los tests con covertura usar:
```
$ coverage run -m unittest discover
```
- Para correr un test en especifico con covertura usar:
```
$ coverage run test_nombre.py
```
- Para ver el resultado de covertura por consola correr:
```
$ coverage report -m
```
- Y para generar los html de los distintos resultados de covertura correr lo siguiente, estos se generan 
en test/htmlcov/:
```
$ coverage html
```
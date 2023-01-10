# proyecto-final-coderhouse
Este proyecto fue realizado con python 3.11 y django 4.1.4

## Pasos para su funcionamiento

1. Verificar si tenemos python

Para comenzar primero tienen que asegurarse que tienen instalado, python.

En windows tiene que abrir una terminal cmd o powershell.
```
PS C:\> python --version 
Python 3.X.X 
```
En Linux/Mac tiene que abrir una terminal bash
```
$ python --version
Python 3.X.X 
```
Si les aparece la versión pueden seguir. Caso contrario descarguen python.

2. Instalar django 

En una terminal cmd o powershell desde windows:
```
C:\> pip install django
```
Linux/Mac:
```
$ pip install django
```
3. Clonar el projecto con GIT

Windows: 
```
C:\> git clone https://github.com/celibodini/My-final-project.git
```
Linux/Mac: 
```
$ git clone https://github.com/celibodini/My-final-project.git
```
4. Correr el servidor

Los siguinetes comandos son analogos en Mac/Linux/Windows:
```
cd My-final-project
python manage.py migrate
```
La consola mostrara las migraciones de la base de datos que se realizaron.

Luego arrancamos el servidor web:
```
python manage.py runserver
```
Hace click en el siguiente link para verlo corriendo:
http://localhost:8000/

En el siguiente link se puede ver el video del funcionamiento del programa: 
https://youtu.be/po9qQJeMZQc

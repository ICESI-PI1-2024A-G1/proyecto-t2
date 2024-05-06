# Proyecto Programacion Academica - Grupo 2/ Proyecto Integrador I
## Integrantes

- Juan Felipe Jojoa A00382042
- Isabela Ocampo A00382369
- Valentina Gonzalez A00394152
- Samuel Alvarez A00394750
- Juan Sebastian Caviedez A00394958
## Introduccion

Bienvenido al repositorio del Modulo de programación académica del Centro Compartido de Servicios Académicos (CCSA). Este proyecto tiene como enfoque el desarrollo de la planeación académica de posgrados para la universidad Icesi, donde se trabaja la gestión de informacion, los servicios de asignacion y la programación semestral de los programas de posgrado.

A continuación la información en detalle del proyecto.
Si desea ver las instrucciones del proyecto dirijase a [Instrucciones de uso](#Instrucciones)

## Contenido del Repositorio

El repositorio esta compuesto por dos carpetas principales (code, src) acompañadas del .gitignore, el cual permite bloquear archivos no deseados en el repositorio.

1. #### [Carpeta Code](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/main/code) 

   La carpeta Code alberga todo el código fuente que crea el proyecto, al igual que la base de datos. 

2. #### [Carpeta Doc](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/main/doc)

   La carpeta doc contiene toda la documentacion del proyecto, listada a continuacion. 

    3. [Mockups](https://www.figma.com/file/iCb75PUrvNJ3AXAyYZ76m2/Pantallas-PI?type=design&node-id=0%3A1&mode=design&t=GYThzBpPmjeEp63h-1)
    5. [Modelo de datos](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/develop/doc/Modelo%20Entidad%20Relaci%C3%B3n)
       El modelo Entidad Relacion representa las conexiones entre los distintos actores del proyecto y como interactuan entre ellos para la obtencion completa de los datos.
    7. [Bitacoras de trabajo](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/IOS-readMe/doc/Bitacoras)
       Las bitacoras de trabajo muestran el flujo de trabajo de los integrantes a traves de los sprints de trabajo. 

    #### Diagramas
    1. [Diagramas de clase UML](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/IOS-readMe/doc/Diagrama%20de%20clases)
    2. [Diagramas de secuencias](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/IOS-readMe/doc/Diagrama%20de%20Secuencia)
    3. [Diagrama de Casos de Uso](https://github.com/ICESI-PI1-2024A-G1/proyecto-t2/tree/IOS-readMe/doc/Diagramas%20de%20casos%20de%20uso)

#### Intruciones de uso{#Instrucciones}
1. Abrir una terminal o Windows Powershell, si le dificulta el uso de comandos, abra la terminal desde la carpeta principal del proyecto.
2. Si no le importa usar comandos, dirijase a la carpeta principal del proyecto a traves de estos.
3. Ejecutar el comando: `.\src\venv\Scripts\activate` para activar el entorno virtual de python configurado.
4. Ejecutar el comando: `python .\src\manage.py makemigrations` para hacer las migraciones de los datos del modelo.
5. Ejecutar el comando: `python .\src\manage.py migrate` para crear las tablas de los modelos.
6. Ejecutar el comando: `python .\src\manage.py runserver` para ejecutar el proyecto.
8. Ir a la url especificada en la consola para acceder a la página.


[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/mxgxu2b2)
